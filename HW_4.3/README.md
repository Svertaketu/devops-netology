# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"

## Обязательные задания
1. Исправленный JSON:
	```json
     { "info" : "Sample JSON output from our service",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : "71.75.34.40"
            },
            { "name" : "second",
            "type" : "proxy",
            "ip": "71.78.22.43"
            }
        ]
    }
    ```
 1. Скрипт:
 ```python
#!/usr/bin/env python3
import sys
import socket
import subprocess
import json
import yaml


def get_url_ip(url):
    url_ip = {}
    for count in range(len(url)):
        exit_code = subprocess.run(['curl', '-Is', str(url[count])],
                                   stdout=subprocess.DEVNULL)
        if exit_code.returncode == 0:
            url_ip[str(url[count])] = socket.gethostbyname(str(url[count]))
    return dict(url_ip)


def write_to_json_and_yaml(s_dict, file_json, file_yaml):
    with open(str(file_json), "w") as js:
        js.write(json.dumps(s_dict, indent=2))
    with open(str(file_yaml), "w") as ym:
        ym.write(yaml.dump(s_dict, indent=2,
                           explicit_start=True,
                           sort_keys=False))


cnt_ask = 0
print('-' * 40)
while 1==1:
    if cnt_ask == 0:
        url_ip_dict = get_url_ip(sys.argv)
        for item_key in url_ip_dict.keys():
            result = item_key + " - " + url_ip_dict[item_key]
            print(result)
        url_ip_dict_coll = url_ip_dict
        cnt_ask = 1
        write_to_json_and_yaml(url_ip_dict, "test5.json", "test5.yaml")
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
        write_to_json_and_yaml(url_ip_dict, "test5.json", "test5.yaml")
    print('-' * 40)
 ```
 