#!/usr/bin/env python

import subprocess

ip = subprocess.Popen('ip link', shell=True, stdout=subprocess.PIPE)
grep1 = subprocess.Popen('grep BROADCAST,MULTICAST,UP,LOWER_UP'.split(), stdin=ip.stdout, stdout=subprocess.PIPE)
ip.stdout.close()
awk1 = subprocess.Popen(['awk','-F',':','{print $2}'], stdin=grep1.stdout, stdout=subprocess.PIPE)
grep1.stdout.close()
iface = awk1.communicate()[0].strip()

ipaddr = subprocess.Popen(['ip','address','show','%s' % iface], stdout=subprocess.PIPE)
grep2 = subprocess.Popen('grep inet'.split(), stdin=ipaddr.stdout, stdout=subprocess.PIPE)
ipaddr.stdout.close()
awk2 = subprocess.Popen("awk '{print $2}'", shell=True, stdin=grep2.stdout, stdout=subprocess.PIPE)
grep2.stdout.close()
awk3 = subprocess.Popen(['awk','-F','/','{print $1}'], stdin=awk2.stdout, stdout=subprocess.PIPE)
awk2.stdout.close()
ipaddress = awk3.communicate()[0].strip()

ipoct = ipaddress[:ipaddress.rfind(".")] + "."

for i in range(1,10):
  ping = subprocess.call('ping -c 1  %s%s' %(ipoct,i),shell=True)
