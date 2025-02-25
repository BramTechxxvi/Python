import datetime

def get_date(userinput):
	pass

def get_description(userinput):
	if not userinput.replace(" ", ""):
		return "Invalid.. input"
	return userinput

def get_amount(userinput):
	while True:
		try: 
			input(userinput)
			if userinput <= 0:
				return "Invalid input... Kindly enter amount again"
			else:
				return "Expense added succesfully"
				break
		except ValueError:		
			return "Invalid"
		
def get_view_expenses(list1, list2, list3):
	if not list1: 
		return "\nNo expenses to view yet... Choose from below"
	else:
		output= "	Date			Description		Amount \n"
		output+= "========================================================================= \n"
		for index in range(len(list1)):
			output+= f"{index+1}.	{list2[index]}		{list1[index]}			{list3[index]} \n"
		output+= "\n ========================================================================= \n"
		return output

def get_totalexpenses(numbers):
	total = 0
	for num in numbers:
		if isinstance(num, str) or num < 0:
			return 'Invalid... input'
		total+= num
	return float(total)

def get_exit():
	return'Thank You for using Semicolon Expense Tracker App'


def main():
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
				date = input(f"Enter date (default:{currentdate}):")

				description = input("Enter description: ")
				addexpense.append(description)
				print(get_description(description))
			case 2:		
				print(get_view_expenses(description, date, amount))
			case 3:
				print(f"\nTotal Expenses is: {get_totalexpenses(addamount)} \n")
			case 4:
				print(get_exit())
				break
			case _:
				print("\nInvalid option... Kindly enter between 1 - 4")
main()