#!/usr/bin/env python
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) #string put inside string

print x
print y

print "I said: %r" % x #string put inside string
print "I also said: '%s'." % y #string put inside string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" #string put inside string
print joke_evaluation % hilarious

w = "This is left side of..."
e = "a string with a right side."

print w + e
