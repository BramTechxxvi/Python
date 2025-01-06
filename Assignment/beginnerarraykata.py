arraysize = int(input("Numbers in array: "))
array = [0] * arraysize
for number in range(arraysize):
    array[number] = int(input("Enter a number: "))
for number in array:
    print(number)
print("\n\nQ1\n")
maximum = array[0]
minimum = array[0]
for number in array:
    if number > maximum:
       maximum = number
    elif number < minimum:
        minimum = number

print(f"Maximum in (array of integers) is: ", maximum)

print("\n\nQ2\n")
print(f"Minimum in (array of integers) is: ", minimum)

print("\n\nQ3\n")
totalsum = 0
for number in array:
    totalsum+= number
    
print(f"The sum of (array of integers) is: {totalsum}")

print("\n\nQ4\n")
sumeven = 0
sumodd = 0
for number in array:
    if number % 2 == 0:
        sumeven +=number
    elif number % 2 != 0:
        sumodd += number
print(f"Sum of even numbers in (array of integers) is: {sumeven}")

print("\n\nQ5\n")
print(f"Sum of odd numbers in (array of integers) is: {sumodd}")

print("\n\nQ6\n")
maxmin = [0] * 2
maxmin[0] = maximum
maxmin[1] = minimum
print(f"[{maximum}, {minimum}]")

print("\n\nQ7\n")
countodd = 0
counteven = 0
for number in array:
    if number % 2 != 0:
        countodd+=1
    elif number % 2 == 0:
        counteven +=1
print(countodd)

print("\n\nQ8\n")
print(counteven)

print("\n\nQ9\n")
evennumber = 0
oddnumber = 0
for number in array:
    if number % 2 == 0:
        evennumber = number
        print(evennumber)

print("\n\nQ10\n")
for number in array:
    if number % 2 != 0:
        oddnumber = number
        print(oddnumber)

print("\n\nQ11\n")
squarenumber = 0
for number in array:
    squarenumber = number ** 2
    print(squarenumber)
    

