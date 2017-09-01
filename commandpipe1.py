#!/usr/bin/env python

import subprocess

command = subprocess.Popen('/sbin/ifconfig eth0'.split(), stdout=subprocess.PIPE)
pipe1 = subprocess.Popen('grep inet'.split(), stdin=command.stdout, stdout=subprocess.PIPE)

command.stdout.close()

print pipe1.stdout.read()
output = pipe1.communicate()[0]
