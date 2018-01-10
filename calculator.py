#!usr/bin/python3

#import a module from the file calc
from calc import sum, mul, div, sub

repeat = 'y'

#loop while the user doesnot has to do more calculations
while(repeat != 'n'):
	#ask the numbers from the user

	
	num1Err = num2Err = 1	#declare two variables to keep track if error occurs. 1 for error occured, 0 for no error


	while(num1Err != 0):	#repeat until the user inputs the correct type of input for first number

		#check if the input number is not a valid real number
		try:
			num1 = float(input("1st Number: "))
			num1Err = 0	#change the error variable to indicate no error occured

		#handle the exception if the user enters a value other than a valid real number
		except ValueError:
			print("Enter a valid number.")

	while(num2Err != 0):	#repeat until the user inputs the correct type of input for the second number

		try:
			num2 = float(input("2nd Number: "))
			num2Err = 0	#change the error variable to indicate no error occured

		except ValueError:
			print("Enter a valid number.")
		
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
	
	#if invalid choice of operation
	else:
		print("Enter a valid character(+, -, *, /)")
	
	#prompt the user if he/she wants to continue or not
	repeat = input("Do you want to continue(y/n)?")

