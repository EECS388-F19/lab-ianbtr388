"""
A script for EECS 388 lab 0
"""

from random import randint

print("Ian Bertram")

def get_random():
	return randint(0, 100)

num_1, num_2 = get_random(), get_random()

print(num_1)
print(num_2)

num_sum = num_1 + num_2 

print("Sum = "+str(num_sum))
print("Average = "+str(num_sum / 2.0))
