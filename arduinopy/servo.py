#!/usr/bin/env python

from pyfirmata import Arduino, util 
from time import sleep
import os

port = "/dev/ttyUSB0"

board = Arduino(port)
sleep(2)

it = util.Iterator(board)
it.start()

servoPin = board.get_pin('d:4:s')
potenPin = board.get_pin('a:0:i')

def turnservo(angle):
	servoPin.write(angle)
	sleep(.020)

try:
	while True:
		sleep(.030)
		analogRead_0 = potenPin.read()
		analogRead_0 = int(((analogRead_0 * 1000) * 180) / 1000)
		turnservo(analogRead_0)
		print analogRead_0
except KeyboardInterrupt:
	board.exit()
	os._exit
