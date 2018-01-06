#!usr/bin/python3

#import a module from the file calc
from calc import sum, mul, div, sub

repeat = 'y'

#loop while the user doesnot has to do more calculations
while(repeat != 'n'):
	#ask the numbers from the user
	num1 = int(input("Enter a number: "))
	num2 = int(input("Enter another number: "))

	#print the menu to the user
	print("Operations: \n>+\n>-\n>*\n>/")
	
	#ask the user's choice
	operator = input("Enter your choice: ")
	
	#for addition
	if(operator == '+'):
		result = sum(num1, num2)
		print("The sum of {} and {} is {}".format(num1, num2, result))
	
	#for subtraction
	elif(operator == '-'):
		result = sub(num1, num2)
		print("The difference of {} and {} is {}".format(num1, num2, result))	

	#for multiplication
	elif(operator == '*'):
		result = mul(num1, num2)
		print("The product of {} and {} is {}".format(num1, num2, result))
	
	#for division
	elif(operator == '/'):
		result = div(num1, num2)
		print("The division of {} and {} is {}".format(num1, num2, result))
	else:
		print("Enter a valid character(+, -, *, /)")
	
	repeat = input("Do you want to continue(y/n)?")

