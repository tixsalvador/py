#!/usr/bin/env python

import subprocess

iplink_cmd = subprocess.check_output(['ip','link']).strip()

lines = (iplink_cmd.splitlines())[2]

iface = lines.split()

iface = iface[1].replace(':','').strip()
print iface
