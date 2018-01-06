#!usr/bin/python3

#returns sum of two numbers
def sum(a, b):
	return (a + b)

#returns difference of two numbers
def sub(a, b):
	return (a - b)

#returns multiplication of two numbers
def mul(a, b):
	return (a * b)

#returns division of two numbers
def div(a, b):
	try:
		return (a / b)
	except ZeroDivisionError as err:
		print("Error ", err) 
