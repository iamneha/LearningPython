#!/usr/bin/env python3
i = 0
numbers = []

while i < 6:
	print("At the top i is", i)
	numbers.append(i)

	i = i + 1
	print("number is now", numbers)

	print("At the bottom i is", i)
print("The numbers:")
for num in numbers:
	print(num)
