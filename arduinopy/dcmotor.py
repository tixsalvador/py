#!/usr/bin/env python

from pyfirmata import Arduino
from time import sleep
import os

port = '/dev/ttyUSB0'
board = Arduino(port)

def motorun(speed,ti):
	motorpin.write(speed)
	sleep(ti)
	motorpin.write(0)

motorpin = board.get_pin('d:3:p')

try:
	while True:
		run = input("Input Speed: ")
		if (run >= 100) or (run <=0):
			print "Values from 0 to 100 only."
			board.exit()
			break
		t = input("Time in sec: ")
		motorun(run,t)
except KeyboardInterrupt:
	board.exit()
	os._exit
