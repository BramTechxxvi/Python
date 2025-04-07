import random
"""
Generate 15 numbers from 50-150
sum all numbers at indices divisible by 4
sum 3 largest number and three smallest number
determine the product if the last five five numbers
"""
tuple_list = tuple()
sum_of_indices_of_four = 0
sum_of_three_largest_and_three_smallest = 0
for num in range(15):
    numbers = random.randint(1, 50)
    tuple_list += (numbers,)
    if num % 4 == 0: sum_of_indices_of_four += tuple_list[num]
print(f"""
    Tuple: {tuple_list}
    Sum of elements at indices divisible by 4: {sum_of_indices_of_four}
    Sum of three largest and three smallest: {sum_of_three_largest_and_three_smallest}
""")