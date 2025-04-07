import random
tuple_list2 = tuple()
odd_result = 0
even_result = 0
sum_of_smallest_and_largest = 0
product = 0
for num in range(20):
    figure = random.randint(1, 50)
    tuple_list2 += (figure,)
    if num % 2 != 0: odd_result += tuple_list2[num]
    if num % 2 == 0: even_result += tuple_list2[num]
largest = tuple_list2[0]
smallest = tuple_list2[0]
for element in tuple_list2:
    if element < smallest: smallest = element
    if element > largest: largest = element
sum_of_smallest_and_largest = smallest + largest
print(f"""
    Tuple : {tuple_list2}
    Sum of elements at odd position: {odd_result}
    Sum of elements at even position: {even_result}
    Sum of smallest and largest: {sum_of_smallest_and_largest}
    product of the first five element: {product}
""")