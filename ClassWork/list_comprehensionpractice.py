def get_even(number):
	if number % 2 == 0: return number

scores = [20, 52, 121, 78, 51, 903, 64]
result = []
for score in scores:
	result.append(get_even(score))
		
result = [score for score in scores get_even(score)]
print(result)