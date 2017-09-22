#!/usr/bin/env python

from pyfirmata import Arduino, util 
from time import sleep
import os

port = '/dev/ttyUSB0'
board = Arduino(port)
sleep(2)

it = util.Iterator(board)
it.start()

analog0 = board.get_pin('a:0:i')
analog1 = board.get_pin('a:1:i')
analog2 = board.get_pin('a:2:i')
digital9 = board.get_pin('d:9:p')
digital10 = board.get_pin('d:10:p')
digital11 = board.get_pin('d:11:p')

def rgbcolor(red, green, blue):
	digital9.write(red)
	digital10.write(blue)
	digital11.write(green)

try:
	while True:
		sleep(.020)
		analog_0 = analog0.read()
		analog_1 = analog1.read()
		analog_2 = analog2.read() 
		rgbcolor(analog_0,analog_1,analog_2)	
except KeyboardInterrupt:
	board.exit()
	os._exit

