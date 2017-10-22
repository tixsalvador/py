#!/usr/bin/env python

import csv

filename = "drivers.csv"

with open(filename) as file_handle:
	reader = csv.reader(file_handle,delimiter=",")
	for i in reader:
		hardware = i[3].strip()
		if hardware == "Display":
			print i[0]+i[1]+i[3]+i[4]+i[5]+i[6]
