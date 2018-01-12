#!usr/bin/python3

#declare a sentece for testing
sentence = input("Enter a sentence: ")

if sentence in open('pos.txt').read():
	print("Positive")
elif sentence in open('neg.txt').read():
	print("Negative")

else:
	print("Not positive neither negative")


