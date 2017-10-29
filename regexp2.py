#!/usr/bin/env python

import re

line = "Nov  4 00:02:40 shirazk2141 sshd[13506]: Invalid user jira from 87.249.204.63"

match = re.search('^(.*?)\s\d{2}\:\d{2}\:\d{2}\s\w+\ssshd.*?user\s(\w+)\sfrom\s(.*$)', line)
print match.groups()
print match.group(1)
print match.group(2)
print match.group(3)
