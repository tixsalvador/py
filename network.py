#!/usr/bin/env python

import subprocess

command = subprocess.Popen('/bin/netstat -r'.split(), stdout=subprocess.PIPE)
pipe1 = subprocess.Popen('grep default'.split(), stdin=command.stdout, stdout=subprocess.PIPE)
command.stdout.close()

pipe2 = subprocess.Popen(['awk','{print $8}'], stdin=pipe1.stdout, stdout=subprocess.PIPE)
pipe1.stdout.close()

iface = pipe2.stdout.read()

output = pipe2.communicate()[0]

command2 = subprocess.Popen("/sbin/ifconfig %s" %iface, shell=True, stdout=subprocess.PIPE)

print command2.stdout.read()



