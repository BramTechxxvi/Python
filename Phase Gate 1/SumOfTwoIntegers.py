first_integer = 12
second_integer = 35
sum = first_integer + second_integer
while True:
	try:
		result = int(input("Enter sum of integers: "))
		if result == str or result <= 0:
			print("Invalid input")
		else:
			break
	except ValueError:
		print("Invalid input")

if sum == result:
	print("True")
else:
	print("False") 
	