>>> line = "Oct  6 23:59:32 campBIGfalcon sshd[945]: Server listening on 0.0.0.0 port 22."
>>> print line
Oct  6 23:59:32 campBIGfalcon sshd[945]: Server listening on 0.0.0.0 port 22.
>>> import re
>>> match = re.search('sshd', line)
>>> print match
<_sre.SRE_Match object at 0x233c2a0>
>>> match = re.search('hello', line)
>>> print match
None
>>> match = re.search('[A-Z][a-z]{2}\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s\w+\ssshd\[\d*\]: Server listening on \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\ port \d*', line)
>>> print match
<_sre.SRE_Match object at 0x233c308>
>>> match = re.search('[A-Z][a-z]{2}\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s\w+\ssshd\[\d*\]: Server listening on \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\ port', line)
>>> print match
<_sre.SRE_Match object at 0x233c370>
>>> match = re.search('[A-Z][a-z]{2}\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s\w+\ssshd\[\d*\]: Server listening on \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\ port \d*', line)
>>> print match
<_sre.SRE_Match object at 0x233c308>
>>> match = re.search('^(.*?)\s(\w+)\ssshd.*?on\s(.*?)\sport.*$', line)
>>> print match
<_sre.SRE_Match object at 0x7fa199d2aa48>
>>> print match.groups()
('Oct  6 23:59:32', 'campBIGfalcon', '0.0.0.0')
