#!/usr/bin/env python

import subprocess

command = subprocess.Popen('/sbin/ifconfig eth0', shell=True, stdout=subprocess.PIPE)

print command.stdout.read()
output = command.communicate()[0]


##################### 1 PIPE ################################################

#!/usr/bin/env python

import subprocess

command = subprocess.Popen('/sbin/ifconfig eth0'.split(), stdout=subprocess.PIPE)
pipe1 = subprocess.Popen('grep inet'.split(), stdin=command.stdout, stdout=subprocess.PIPE)

command.stdout.close()

print pipe1.stdout.read()
output = pipe1.communicate()[0]

############################################################################

##################### 2 PIPE ################################################

#!/usr/bin/env python

import subprocess

command = subprocess.Popen('/sbin/ifconfig eth0'.split(), stdout=subprocess.PIPE)
pipe1 = subprocess.Popen('grep inet'.split(), stdin=command.stdout, stdout=subprocess.PIPE)
command.stdout.close()

pipe2 = subprocess.Popen(['awk', '{print $2}'], stdin=pipe1.stdout, stdout=subprocess.PIPE)
pipe1.stdout.close()



print pipe2.stdout.read()
output = pipe2.communicate()[0]


############################################################################

##################### 3 PIPE ################################################

#!/usr/bin/env python

import subprocess

command = subprocess.Popen('/sbin/ifconfig eth0'.split(), stdout=subprocess.PIPE)
pipe1 = subprocess.Popen('grep inet'.split(), stdin=command.stdout, stdout=subprocess.PIPE)
command.stdout.close()

pipe2 = subprocess.Popen(['awk', '{print $2}'], stdin=pipe1.stdout, stdout=subprocess.PIPE)
pipe1.stdout.close()

pipe3 = subprocess.Popen(['awk', '-F', ':','{print $2}'], stdin=pipe2.stdout, stdout=subprocess.PIPE)
pipe2.stdout.close()

print pipe3.stdout.read()
output = pipe3.communicate()[0]

########################################################################################################
