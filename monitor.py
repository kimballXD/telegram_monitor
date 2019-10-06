# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:30:58 2019

@author: Wu
"""

import sys
from os.path import isdir, isfile, join
from os import mkdir
from re import findall
from datetime import datetime
from yaml import load
from requests import request
from time import sleep
from bs4 import BeautifulSoup as bs

def getSoup (url,method, rest=0, returnRep=False, **kwargs):
    rep = request(method, url, **kwargs)    
    sleep(rest)
    rep.encoding = 'utf8'
    soup = bs(rep.text,'lxml')
    if returnRep:
        setattr(soup,'rep',rep)
    return soup


#%% parse config
with open('config.yaml','r') as con:
    config = load(con)    
task = sys.argv[1] if len(sys.argv)>1 else 'default'
page_name, page_url = config[task]['page_name'], config[task]['page_url']

#%% crawl and parse data    
soup = getSoup(page_url, 'get')
cur_stat = soup.select('.tgme_page_extra')[0].text.replace(' ','')
info = findall('\d+', cur_stat)
cur = 'NA' if len(info)==1 else info[1]
total = info[0]
d, t = datetime.now().strftime('%Y/%m/%d %H:%M:%S').split()
res= [d, t, cur, total]

#%% data dump
msg = '[{} {}] Member status: {}/{}'.format(*res)
write_msg = '\t'.join(res) + '\n'

if not isdir('data'):
    mkdir('data')    
data_path = join('data', page_name +'.txt')
method = 'w' if not isfile(data_path) else 'a'    
with open(data_path, method) as out:
    out.write(write_msg)
print(msg)