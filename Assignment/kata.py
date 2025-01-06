print("Q1")
def is_even(number):
	return number % 2 == 0
figure = int(input("Enter an integer: "))

print(f"is {figure} even?  {is_even(figure)}")


print("\nQ2")



print("\nQ3")
def subtract(x, y):
	return abs(x - y)
x = int(input("Enter an integer: "))
y = int(input("Engter an integer: "))

print(f"Answer is {subtract(x, y)}")


print("\nQ4")
def divide(v, w):
	return (v / w)
v = int(input("Enter an integer: "))
w = int(input("Enter an integer: "))

print(f"result is {divide(v, w)}")


print("\nQ5")



print("\nQ6")
def square(number):
	if number < 0:
   		return False
	return number ** 2 != 0
number = int(input("Enter an integer: "))

print(f" is {number} a square number  {square(number)}")


print("\nQ7")
def is_palindrome(number):
	return number == number[::-1]
number= str(input("Enter five digits integer: "))
print(f"is {number} a palindrom integer  {is_palindrome(number)}")


print("\nQ8")



print("\nQ9")
def square(number):
	return number ** 2
number = int(input("Enter an integer: "))

print(f"The square of {number} is  {square(number)}")


	
