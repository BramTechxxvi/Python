print("Q1 Return largest in list \n")
def get_largest(number_list):
	largest = number_list[0]
	for index in number_list:
		if index > largest:
			largest = index
	return largest

largest_input = [56, 78, 5000, 8, 21, 90, 17, 132]
print(f"Largest element is: {get_largest(largest_input)} \n\n")


print("Q2 Reverse a list \n")
def get_reverse(reverse_list):
	temp = reverse_list[::-1]
	return temp
reverse_input = [56, 78, 5000, 8, 21, 90, 17, 132]
print(get_reverse(reverse_input))
	  

print("\n\nQ3 Check if an element occurs \n")
def get_check_element(number_list, search):
	for index in number_list:
		if index == search:
			return True
	return False
	
element_input= int(input("Enter a number to check: "))
element_list = [56, 8, 500, 18, 12, 90, 1, 32]
print(f"Check if {element_input} in the list: {get_check_element(element_list, element_input)} \n\n")

	
print("Q4 Odd positions \n")
def get_odd_positions(number_list):
	odd_element = []
	for index in range(len(number_list)):
		if index % 2 != 0:
			odd_element.append(number_list[index])
	return odd_element

odd_list_input = [89, 35, 18, 9, 400, 6, 24]
print(f"Elements in odd positions are: {get_odd_positions(odd_list_input)} \n\n")


print("Q5 Even positions \n")
def get_even_positions(number_list):
	even_element = []
	for index in range(len(number_list)):
		if index % 2 == 0:
			even_element.append(number_list[index])
	return even_element

even_list_input = [89, 35, 18, 9, 400, 6, 24]
print(f"Elements in even positions are: {get_even_positions(even_list_input)} \n\n")


print("Q6 Total of running a list \n")
def get_running_total(number_list):
	total = 0
	running_total = []
	for index in number_list:
		total+=index
		running_total.append(total)
	return running_total

list_input = [89, 35, 18, 9, 400, 6, 24]
print(f"Running total is: {get_running_total(list_input)}\n\n")


print("Q7 String is Palindrome \n")
def get_is_palindrome(words):
	if  words== words[::-1]:
		return True
	return False

is_palindrome_input = input("Enter a string of numbers: ")
print(f"Check if String is Palindrome: {get_is_palindrome(is_palindrome_input)} \n\n")


print("Q8(i) Sum of list using for-loop \n")
def get_sum1(numbers_list):
	total = 0
	for index in numbers_list:
		total+= index
	return total

for_loop_input = [56, 78, 5000, 8, 21, 90, 17, 132]
print(f"For loop total: {get_sum1(for_loop_input)} \n\n")


print("Q8(ii) Sum of list using while-loop \n")
def get_sum2(number_list):
	total = 0
	index = 0
	while index < len(number_list):
		total+=number_list[index]
		index = index +1
	return total
	
while_loop_input = [56, 78, 5000, 8, 21, 90, 17, 132]
print(f"while loop total: {get_sum1(while_loop_input)} \n\n")


print("Q9 Concat two list \n")
def get_concat(list1, list2):
	list3 = list1 +list2
	return list3
concat_input1 = ['a', 'b', 'c']
concat_input2 = [12, 13, 14]
print(f"Concatenated list: {get_concat(concat_input1, concat_input2)} \n\n")


print("Q10 Combine list")
def get_combine(list1, list2):
	index = 0
	result =[]
	list3 = len(list1) + len(list2)
	while index < list3:
		if index < len(list1):
			result.append(list1[index])
		if index < len(list2):
			result.append(list2[index])
		index = index +1
	return result
	
combine_input1 = ['a', 'b', 'c']
combine_input2 = [12, 13, 14]
print(f"Combined list: {get_combine(concat_input1, concat_input2)} \n\n")

print("Q11 ")
def get_list(number):
	number_list = []
	for index in number:
		number_list.append(index)
	return number_list

number_input = input("Enter a number: ")
print(f"List of digits: {get_list(number_input)}")