#!/usr/bin/env python
def cheese_and_crackers(cheese_count, boxes_of_crackers):  #define function
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Man that's enough for party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30) #call function

print "Or we can use variable from our script:"
amount_of_cheese = 10    #declare variables
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)  

print "We can even do maths also:"
cheese_and_crackers(10 + 20, 5 + 6) #some math calculation

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #combine math and variables

print "We can combine two variables also"
cheese = 50
crackers = 100
cheese_and_crackers(amount_of_cheese + cheese, amount_of_crackers + crackers)

print "Now it's user turn to choose amount of cheese and crackers"
cheese1 = int(raw_input("amount of cheese you want = "))
crackers1 = int(raw_input("amount of crackers you want = "))
cheese_and_crackers(cheese1, crackers1)
