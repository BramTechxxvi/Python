while True:
	try:
		number = int(input("Enter an integer between 0 - 1000: "))
		if number < 0 or number > 1000:
			print("Invalid input")
		else:
			break
	except ValueError:
		print("invalid input")
last_number = number % 10
two_digit = number // 10
second_number = two_digit % 10
first_number = two_digit // 10
sum = last_number + second_number + first_number
print(sum)