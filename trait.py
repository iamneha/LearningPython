'''
Given a number find the number of trailing zeroes in its factorial.

Input Format

A single integer - N

Output Format

Print a single integer which is the number of trailing zeroes.

Input Constraints

1 <= N <= 1000


SAMPLE INPUT 
10
SAMPLE OUTPUT 
2
Explanation
10! = 3628800 has 2 zeros in the end.
'''

n = int(raw_input())
if n<5:
	print(0)
else:
	print(n/5)
