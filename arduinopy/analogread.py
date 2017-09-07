#!/usr/bin/env python

from pyfirmata import Arduino, OUTPUT, INPUT, util
from time import sleep
import os

port = '/dev/ttyUSB0'

board = Arduino(port)

it = util.Iterator(board)
it.start()

board.digital[13].mode = OUTPUT

analogpin = board.get_pin('a:0:i')

try:
	while True:
		pindata = analogpin.read()
		print pindata

except KeyboardInterrupt:
	board.exit()
	os._exit()



