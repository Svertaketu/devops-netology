#!/usr/bin/env python3

import os

bash_command = ["cd ~/PycharmProjects/netology/devops-netology", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('изменено') != -1:
        prepare_result = result.replace('\t изменено:   ', '')
        print(prepare_result)
        break
