#!/usr/bin/env python

import csv
filename = "storelist.csv"

with open (filename, "r") as f:
#	readr = csv.reader(f, delimiter=",")
#	for i in readr:
#		print i[0],i[1],i[2] 
	firstcolumn = [line.split(',') for line in f]

	for i in firstcolumn:
		print i[0],i[1],i[2]
f.close()
