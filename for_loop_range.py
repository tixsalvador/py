#!/usr/bin/env python

import subprocess

for i in range(1,11):
        command = subprocess.call('ping -c 1 10.5.1.%s' %(i), shell=True)
