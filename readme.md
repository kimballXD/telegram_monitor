# Telegram Group Invitation Page Monitor

Record the number of members of telegram groups, where the numbers extract from group invitation page.
Every execution will save a new entry into the correspondent local data file. 

## Usage

1. Set the `task_name`, `page_name` and `page_url` variables in the `config.yaml`
    - You can set as many tasks as you want. 
    - However, every execution will limit to just execute ONE task.
    
2. Execute `monitor.exe` with the argument `{task_name}`
    - if leave blank, the program will execute `default` task.
    
3. Recored data will be saved to a table-delimited file named `{page_name}.txt` in `data` folder, with four columns:
    - date (YYYY/mm/dd)
    - time (HH:MM:SS)
    - number of current online member
    - number of total member
    


