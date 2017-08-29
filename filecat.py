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


# With output write on a file

#!/usr/bin/env python

filewrite = open("stores","w")
with open ("storelist.csv","r") as f:
        storeno = [line.split(',')[0] for line in f]
        for i in storeno:
                filewrite.write(i + "\n")
filewrite.close()
