#!/usr/bin/env python
from sys import argv

script, filename = argv

txt = open(filename)

print "here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file1 = raw_input(">")
txt = open(file1) #open file
print txt.read() #read the file

