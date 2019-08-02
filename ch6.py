#!/usr/bin/python

import zipfile
import re

f_dir = r'E:\Project\python\channel.zip'
f_z = zipfile.ZipFile(f_dir)
print f_z.read("readme.txt")
com = re.compile(r'Next nothing is (\d+)')
first = '90052'
comments = []

while True:
    content = f_z.read(first + '.txt')
    comments.append(f_z.getinfo(first + '.txt').comment) 
    match = re.match(com,content)
    if match == None:
        break
    first = match.group(1)

print ''.join(comments)
