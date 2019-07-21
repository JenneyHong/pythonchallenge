#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# http://www.pythonchallenge.com/pc/def/equality.html
#
#
# One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
# find a word its' letter all surrounded by three big letter like "AAAaAAA" from this string 
import urllib


file = urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
s = file.read()

def lower(x):
	return x >= 'a' and x <= 'z'

def upper(x):
	return x >= 'A' and x <= 'Z'

letter = ""
for i in range(4, len(s)+4):
	if lower(s[i-4]) and upper(s[i-3]) and upper(s[i-2]) and upper(s[i-1]) and lower(s[i]) and upper(s[i+1]) and upper(s[i+2]) and upper(s[i+3]) and lower(s[i+4]):
		letter += s[i]

print letter

print "Next challenge go to website http://www.pythonchallenge.com/pc/def/%s.php" % letter

# Next challenge go to website http://www.pythonchallenge.com/pc/def/linkedlist.php
