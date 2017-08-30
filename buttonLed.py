#!/usr/bin/env python

import pyfirmata
from time import sleep

def blinkled(pin):
	board.digital[pin].write(1)
	sleep(1)
	board.digital[pin].write(0)
	sleep(1)

port = "/dev/ttyUSB0"
board = pyfirmata.Arduino(port)

it = pyfirmata.util.Iterator(board)
it.start()

buttonpin = board.get_pin('d:3:i')
yellowpin = 13
redpin = 6

while True:
	value=buttonpin.read()
	print (value)

	if value is True:
		blinkled(yellowpin)
	else:
		blinkled(redpin)

board.exit()
		
		
