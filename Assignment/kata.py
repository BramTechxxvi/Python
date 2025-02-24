print("Q1 isEven")
def get_is_even(number):
	if number == 0:
		return False
	return number % 2 == 0

is_even_input = int(input("Enter a number: "))
print(f"Is {is_even_input} an even number?  {get_is_even(is_even_input)}")


print("\nQ2 isPrime")
def get_is_prime(number):
	if number <= 1:
		return False
	if number == 2:
		return True
	for num in range(2, number +1):
		if number % num == 0:
			return False
		else:
			return True
	return True
		
is_prime_input = int(input("Enter a number: "))
print(f"Is {is_prime_input} a prime number? {get_is_prime(is_prime_input)}")


print("\nQ3 Subtract")
def get_subtract(firstnumber, secondnumber):
	return abs(firstnumber - secondnumber)

subtract_input1 = int(input("Enter an integer: "))
subtract_input2 = int(input("Engter an integer: "))
print(f"The difference is: {get_subtract(subtract_input1, subtract_input2)}")


print("\nQ4 Divide")
def get_divide(firstnumber, secondnumber):
	result = 0
	if secondnumber == 0:
		result = 0
	else:
		result = firstnumber / secondnumber
	return result 

divide_input1 = int(input("Enter an integer: "))
divide_input2 = int(input("Enter an integer: "))
print(f"result is {get_divide(divide_input1, divide_input2)}")


print("\nQ5 Factors of integer")
def get_factor(number):
	count = 0
	for num in range(1, number +1):
		if number % num == 0:
			count = count + 1
	return count

factors_input = int(input("Enter a number: "))
print(f"Factors of {factors_input} are: {get_factor(factors_input)}")

print("\nQ6 is a Square number?")
def get_is_square(number):
	if number < 0:
		return False
	return number ** 2 != 0

is_square_input = int(input("Enter an integer: "))
print(f" is {is_square_input} a square number  {get_is_square(is_square_input)}")


print("\nQ7 isPalindrome")
def get_is_palindrome(number):
	return number == number[::-1]

palindrome_input = input("Enter five digits integer: ")
print(f"is {palindrome_input} a palindrom integer  {get_is_palindrome(palindrome_input)}")


print("\nQ8 Factorial")
def get_factorial(number):
	total = 1
	for num in range(1, number +1):
		total *= num
	return total

factorial_input = int(input("Enter a number: "))
print(f"Factorial of {factorial_input} is: {get_factorial(factorial_input)}")
	

print("\nQ9 Square of number")
def get_square_of(number):
	return number ** 2

square_input = int(input("Enter an integer: "))
print(f"The square of {square_input} is: {get_square_of(square_input)}")