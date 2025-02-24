def get_riders_wage(number1):
	amount_per_parcel = 0
	base_pay = 5000

	if number1 < 50:
		amount_per_parcel = 160
	elif number1 <= 59:
		amount_per_parcel = 200
	elif number1 <= 69:
		amount_per_parcel = 250
	else:
		amount_per_parcel = 500
	riders_wage = (number1 * amount_per_parcel) + base_pay
	return riders_wage


def main():
	while True:
		try:
			collection_rate = int(input("Enter successful delivery: "))
			if collection_rate > 0: break
			else: print("\nInvalid input... Kindly enter again")
		except ValueError:
			print("\nInvalid input... Kindly enter again")
	print(f"Rider's Wage = {get_riders_wage(collection_rate)}")

if __name__=="__main__":
	main()