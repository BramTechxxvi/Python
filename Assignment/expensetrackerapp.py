import datetime

def get_totalexpenses(numbers1):
	total = 0
	for num in numbers1:
		if isinstance(num, str) or num < 0: print("Invalid input")
		total+= num
	return total

addexpense = []
addamount = []
addate = []
currentdate = datetime.date.today()
print("	Welcome to Semicolon Expense Tracker App 	\n======================================== \n")

while True:
	try:	
		choice = int(input("1. Add an expense \n2. View all expense \n3. Calculate total expenses \n4. Exit \n\nSelect an option: "))
	except ValueError:
			print("\nInvalid input... Enter only numerical value")
			continue
	match choice:
		case 1:
			date = input(f"Enter date (default:{currentdate}) :")
			if date.isalpha() or date.isdigit():
				date = str(currentdate)
				print("\nInvalid Input... using default date")
			addate.append(date)
			while True:
					description = input("Enter description: ")
					if description.isalpha(): 
						addexpense.append(description)
						break
					else: print("\nInvalid input. Enter ony alphabets")
			while True:
				try:
					amount = float(input("Enter amount: "))
					if amount <= 0: print("\nInvalid input... Kindly enter amount again")
					else:
						addamount.append(amount)
						print("\nExpense added succesfully \n")
						break
				except ValueError:
					print("\nInvalid input... Enter amount again")
		case 2:		
			if not addexpense: print("\nNo expenses to view yet... Choose from below")
			else:
				print("Date			Description		Amount")
				print("===============================================================")
				for index in range(len(addexpense)):
					print(f"{addate[index]}		{addexpense[index]}		{addamount[index]}")
				print("===============================================================")
		case 3:
			print(f"\nTotal Expenses is: {get_totalexpenses(addamount)} \n")
		case 4:
			print("Thank You for using Semicolon Expense Tracker App")
			break
		case _:
			print("\nInvalid option... Kindly enter between 1 - 4")