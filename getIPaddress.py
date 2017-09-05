#!/usr/bin/env python

import subprocess

command = subprocess.Popen('ip link',shell=True, stdout=subprocess.PIPE)
pipe1 = subprocess.Popen('grep BROADCAST'.split(), stdin=command.stdout, stdout=subprocess.PIPE)
command.stdout.close()
pipe2 = subprocess.Popen(['awk', '-F', ':', '{print $2}'], stdin=pipe1.stdout, stdout=subprocess.PIPE)
pipe1.stdout.close()

iface = pipe2.communicate()[0].strip()

command2 = subprocess.Popen(['/sbin/ifconfig', '%s' %iface], stdout=subprocess.PIPE)
grep = subprocess.Popen(['grep', 'inet'], stdin=command2.stdout, stdout=subprocess.PIPE)
command2.stdout.close()
awk = subprocess.Popen(['awk', '-F', ':', '{print $2}'], stdin=grep.stdout, stdout=subprocess.PIPE)
grep.stdout.close()
awk2 = subprocess.Popen("awk '{print$1}'", shell=True, stdin=awk.stdout, stdout=subprocess.PIPE)
awk.stdout.close()

ipaddress =  awk2.communicate()[0].strip()

ipoct = ipaddress.split('.')

firstoctet = ipoct[0]
secondoctet = ipoct[1]
thirdoctet = ipoct[2]
fourthoctet = ipoct[3]

for i in ipoct:
        print i
