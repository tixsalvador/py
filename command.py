#!/usr/bin/env python

import subprocess

command = subprocess.Popen('/sbin/ifconfig eth0', shell=True, stdout=subprocess.PIPE)

print command.stdout.read()
output = command.communicate()[0]
