#!/usr/bin/env python
def add(a, b):
	print "ADDING %d + %d " % (a, b)
	return a + b
def sub(a, b):
	print "SUBTRACT %d + %d" % (a, b)
	return a - b
def mul(a, b):
	print "Multiply %d * %d" % (a, b)
	return a * b
def div(a, b):
	print "DIVIDE %f / %f" % (a, b)
	return a / b

age = add(30, 5)
height = sub(78, 4)
weight = mul(90, 2)
iq = div(100, 2)
print "Age: %d, Height: %d, weight: %d, IQ: %f" % (age, height, weight, iq)
print "Here is puzzle"
what = add(age, sub(height, mul(weight, div(iq, 2))))
print "That becomes:", what, "can you do it by hand"
