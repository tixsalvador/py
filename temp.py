#!/usr/bin/env python

def user_input():
  temp = float(raw_input("What is the temp? "))
  scale = raw_input("Is it in Celcius or Fahrenheit? ").lower().strip()
  return (temp,scale)


def compute(temp,scale='celsius'):
  if scale == 'celcius':
     conv = temp * 9/5 +32
     x = 'F'
  else:
     conv =  (temp - 32) * 5/9
     x = 'C'
  print "%s %s is converted to %s %s" % (temp,scale,conv,x)

while True:
  temp,scale = user_input()
  if scale.startswith('c'):
    compute(temp,scale='celcius')
    break
  elif scale.startswith('f'):
    compute(temp,scale='fahrenheit')
    break
  else:
    print ("CELSIUS and FAHRENHEIGHT ONLY!!")
