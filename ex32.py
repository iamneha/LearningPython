#!/usr/bin/env python3
count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in count:
	print("This is count ", number) 
#same as above
for fruit in fruits:
	print("A fruit of type:", fruit) 

#we can also go through mixed lists too
#notice we have to use %r since we don't know what's n it
for i in change:
	print("i got ", i)

#we could also build lists, first start with an empty element
elements = []
for i in range(0, 6):
	print("Adding", i , "to the list") 
	elements.append(i)

for i in elements:
	print("Element was:", i) 
