# Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"

## Обязательные задания

1.  Скрипт:
	```python
    #!/usr/bin/env python3
	a = 1
	b = '2'
	c = a + b
	```
    * Ошибка, нельзя складывать целочисленное и строку.
    * Объявляем a = '1', b = '2', получаем c = 12
    * Объявляем a = 1, b = 2, получаем c = 3
    

1.  Скрипт:
    ```python  
    #!/usr/bin/env python3
      
    import os
    
    bash_command = ["cd ~/PycharmProjects/netology/devops-netology", "git status"]
    result_os = os.popen(' && '.join(bash_command)).read()
    
    for result in result_os.split('\n'):
        if result.find('изменено') != -1:
            prepare_result = ' ' +  bash_command[0].replace('cd ','')\
                      + '/' + result.replace('\tизменено:      ', '')
            print(prepare_result)
    ```
1. Скрипт:
   ```python
   #!/usr/bin/env python3

   import os
   import sys

   test_path = sys.argv[1]
   bash_command = ["cd " + test_path, "git status"]
   result_os = os.popen(' && '.join(bash_command)).read()

   for result in result_os.split('\n'):
       if result.find('изменено') != -1:
           prepare_result = ' ' + bash_command[0].replace('cd ', '') \
                            + result.replace('\tизменено:      ', '/')
           print(prepare_result)
   ```
1. Скрипт принимает <URL сервиса> как входной параметр.(drive.google.com mail.google.com google.com)

   ```python
   #!/usr/bin/env python3
   import sys
   import socket
   import subprocess
   import time
   
   
   def get_url_ip(url):
       url_ip = {}
       for count in range(len(url)):
           exit_code = subprocess.run(['curl', '-Is', str(url[count])],
                                      stdout=subprocess.DEVNULL)
           if exit_code.returncode == 0:
               url_ip[str(url[count])] = socket.gethostbyname(str(url[count]))
       return dict(url_ip)
   
   
   cnt_ask = 0
   print('-' * 40)
   while cnt_ask < 100:
       if cnt_ask == 0:
           url_ip_dict = get_url_ip(sys.argv)
           for item_key in url_ip_dict.keys():
               result = item_key + " - " + url_ip_dict[item_key]
               print(result)
           url_ip_dict_coll = url_ip_dict
       else:
           url_ip_dict = get_url_ip(sys.argv)
           for item_key in url_ip_dict.keys():
               if url_ip_dict[item_key] == url_ip_dict_coll[item_key]:
                   result = item_key + " - " + url_ip_dict[item_key]
                   print(result)
               else:
                   result = "[ERROR] " + item_key + " IP mismatch: " \
                            + url_ip_dict_coll[item_key] + " --> " \
                            + url_ip_dict[item_key]
                   print(result)
           url_ip_dict_coll = url_ip_dict
       print('-' * 40)
       cnt_ask += 1
       time.sleep(1)
   ```