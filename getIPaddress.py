#!/usr/bin/env python

import subprocess

command = subprocess.Popen('ip link',shell=True, stdout=subprocess.PIPE)
pipe1 = subprocess.Popen('grep BROADCAST,MULTICAST,UP,LOWER_UP'.split(), stdin=command.stdout, stdout=subprocess.PIPE)
command.stdout.close()
pipe2 = subprocess.Popen(['awk', '-F', ':', '{print $2}'], stdin=pipe1.stdout, stdout=subprocess.PIPE)
pipe1.stdout.close()

iface = pipe2.communicate()[0].strip()

command2 = subprocess.Popen('ip addr', shell=True, stdout=subprocess.PIPE)
grep1 = subprocess.Popen('grep inet'.split(), stdin=command2.stdout, stdout=subprocess.PIPE)
command2.stdout.close()
grep2 = subprocess.Popen(['grep', '%s' %iface], stdin=grep1.stdout, stdout=subprocess.PIPE)
grep1.stdout.close()
awk1 = subprocess.Popen("awk '{print $2}'", shell=True, stdin=grep2.stdout, stdout=subprocess.PIPE)
grep2.stdout.close()
awk2 = subprocess.Popen(['awk', '-F', '/', '{print $1}'], stdin=awk1.stdout, stdout=subprocess.PIPE)
awk1.stdout.close()

ipaddr = awk2.communicate()[0].strip()

ipoct = ipaddr.split('.')

firstoct = ipoct[0]
secondoct = ipoct[1]
thirdoct = ipoct[2]
fourthoct = ipoct[3]

print firstoct + "." + secondoct + "." + thirdoct + "." + fourthoct
