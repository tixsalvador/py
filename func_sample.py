#!/usr/bin/env python

import subprocess

def activeProcess(lookup_user,lookup_cmd):
	process_running_all = 0
	process_running_search = 0
	for line in subprocess.check_output("ps -ef", shell=True).splitlines()[1:]:
		user = line.split()[0]
		if lookup_user == user:
			process_running_all+=1
			if lookup_cmd in line:
				process_running_search+=1
	return process_running_all, process_running_search

process_total, process_searched = activeProcess('root','xfs')
print process_total, process_searched
