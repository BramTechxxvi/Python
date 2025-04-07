even_list = []
even_dict ={} 
for number in list(range(0, 31, 2)):
	even_list.append(number)
	even_dict[number]= number * number * number

print(even_list)
print(even_dict)
			