print("Q1 \n")
number_list = [56, 78, 5, 8, 21, 90, 17, 32]
largest = number_list[0]
smallest = number_list[0]
for x in number_list:
	print(x)
	if x > largest:
		largest = x
	if x < smallest:
		smallest = x
print(f"Largest element is: {largest}\n\n")

print("Q2 \n")
print(f"Smallest element is: {smallest}\n\n")

print("Q3 \n")
elementchecker = int(input("Enter a number to check: "))
for x in number_list:
	if elementchecker == x:
		print(f"Element ({elementchecker}) is in the list")
	
print("\n\nQ4 \n")
print("Odd numbers are:")
odd = number_list[0]
for x in number_list:
	if x % 2 != 0:
		odd = x
		print(odd)

print("\n\nQ5 \n")
print("Even numbers are:")
even = number_list[0]
for x in number_list:
	if x % 2 == 0:
		even = x
		print(even)

print("\n\nQ6 \n")
total_sum = sum(number_list)
print(f"Total is: {total_sum}\n\n")

print("\n\nQ7 \n")
ifpalindrome = "12322"
if ifpalindrome == ifpalindrome[::-1]:
	print(f"{ifpalindrome} is palindrome\n\n")
else: 
	print(f"{ifpalindrome} is not Palindrome\n\n")

print("\n\nQ8 \n")
forsum = 0
for x in number_list:
	forsum+= x
print(f"For loop total {forsum}\n")

whilesum = 0
count = 0
while count < len(number_list):
	whilesum+=number_list[count]
	count+=1
print(f"While loop total {whilesum}\n")

print("\n\nQ9 \n")


