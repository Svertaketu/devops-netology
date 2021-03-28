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

