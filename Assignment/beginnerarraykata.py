print("Q1 Return largest element \n")
def get_largest(list1):
    largest = list1[0]
    for number in list1:
         if number > largest:
            largest = number
    return largest

largest_input = [73, 90, 2, 70, -3, 210, 12]
print(f"Largest is: {get_largest(largest_input)} \n\n")


print("Q2 Return smallest element \n")
def get_smallest(list1):
    smallest = list1[0]
    for number in list1:
        if number < smallest:
            smallest = number
    return smallest

smallest_input = [73, 90, 2, 70, -3, 210, 12]
print(f"Smallest element is: , {get_smallest(smallest_input)} \n\n")


print("Q3 Sum of elements in list \n")
def get_total_sum(list1):
    total = 0
    for number in list1:
        total += number
    return total

total_sum_input = [2, 4, 6, 8]
print(f"The sum of elements is: {get_total_sum(total_sum_input)} \n\n")


print("Q4 Sum of even elements \n")
def get_even_sum(list1):
    even_sum = 0
    for number in list1:
        if number % 2 == 0:
            even_sum +=number
    return even_sum

even_sum_input = [34, 11, 17, 19, 18 , 2]
print(f"Sum of even numbers is: {get_even_sum(even_sum_input)} \n\n")


print("Q5 Sum of odd numbers \n")
def get_odd_sum(list1):
    odd_sum = 0
    for number in list1:
        if number %2 != 0:
            odd_sum+=number
    return odd_sum

odd_sum_input = [34, 11, 17, 19, 18 , 2]
print(f"Sum of odd numbers is: {get_odd_sum(odd_sum_input)} \n\n")


print("Q6 Largest and smallest \n")
def get_maxmin(list1):
    largest = list1[0] 
    smallest = list1[0]
    for number in list1:
        if number > largest:
            largest = number
        if number< smallest:
            smallest = number
    return [largest, smallest]
          
maxmin_input = [34, 11, 17, 19, 18 , 2, 1]
print(f" Maximum and minimum is: {get_maxmin(maxmin_input)} \n\n")


print("\n\nQ7\n")
def get_num_of_odd(list1):
    count = 0
    for number in list1:
        if number % 2 != 0:
            count = count +1
    return count

num_of_odd_input1 = [34, 11, 17, 19, 18 , 2, 1]
print(f"Numbers of odd element: {get_num_of_odd(num_of_odd_input1)}")


print("\n\nQ8\n")
def get_num_of_even(list1):
    count = 0
    for number in list1:
        if number % 2 == 0:
            count = count +1
    return count

num_of_even_input = [34, 11, 17, 19, 18 , 2, 1]
print(f"Numbers of even element is: {get_num_of_even(num_of_even_input)} \n\n")


print("Q9 Even numbers\n")
def get_even_numbers(list1):
    even_number =[]
    for number in list1:
        if number % 2 == 0:
            even_number.append(number)
    return even_number

even_numbers_input = [34, 11, 17, 19, 18 , 2, 1]
print(f"List of even numbers: {get_even_numbers(even_numbers_input)} \n\n")


print("Q10 Odd numbers\n")
def get_odd_numbers(list1):
    odd_number = []
    for number in list1:
        if number % 2 != 0:
            odd_number.append(number)
    return odd_number

odd_numbers_input = [34, 11, 17, 19, 18 , 2, 1]
print(f"List of odd numbers: {get_odd_numbers(odd_numbers_input)} \n\n")


print("Q11 Square of elements \n")
def get_square(list1):
    square_number = []
    for number in list1:
        square_number.append(number ** 2)
    return square_number

square_input = [3, 11, 17, 10, 18 , 2, 1]
print(f"Square of elements: {get_square(square_input)} ")