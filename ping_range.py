#!/usr/bin/env python

import subprocess

command1 = subprocess.Popen('ip addr', shell=True, stdout=subprocess.PIPE)
grep1 = subprocess.Popen('grep BROADCAST,MULTICAST,UP,LOWER_UP'.split(), stdin=command1.stdout, stdout=subprocess.PIPE)
command1.stdout.close()
awk1 = subprocess.Popen(['awk','-F',':','{print $2}'], stdin=grep1.stdout, stdout=subprocess.PIPE)
grep1.stdout.close()
ipadd = awk1.communicate()[0].strip()

command1 = subprocess.Popen(['ip','addr','show','%s' %ipadd], stdout=subprocess.PIPE)
grep2 = subprocess.Popen('grep -w inet'.split(), stdin=command1.stdout, stdout=subprocess.PIPE)
command1.stdout.close()
awk2 = subprocess.Popen(['awk','{print $2}'], stdin=grep2.stdout, stdout=subprocess.PIPE)
grep2.stdout.close()
awk3 = subprocess.Popen(['awk','-F','/','{print $1}'], stdin=awk2.stdout, stdout=subprocess.PIPE)
awk2.stdout.close()
ip = awk3.communicate()[0].strip()

ipoct = ip[:ip.rfind(".")] + "."

for i in range(1,10):
	print "IP %s%s" %(ipoct,i)
	subprocess.call('ping -c 1 %s%s' %(ipoct,i), shell=True)
	print " "
