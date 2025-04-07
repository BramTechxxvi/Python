import datetime

def get_date(user_date, current_dates):
	pass

def get_description(userinput):
	while True:
		if not userinput.strip():
			return "Invalid... input"
		else:
			break
	return userinput

def get_amount(userinput):
	while True:
		try: 
			input(userinput)
			if userinput <= 0:
				return "Invalid input... Kindly enter amount again"
			elif isinstance(userinput, str):
				return "invalid input"
				
			else:
				return "Expense added successfully"
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

def get_total_expenses(numbers):
	total = 0
	for num in numbers:
		if isinstance(num, str) or num < 0:
			return 'Invalid input...'
		total+= num
	return float(total)

def get_exit():
	return'Thank You for using Semicolon Expense Tracker App'


def main():
	add_expense = []
	add_amount = []
	add_date = []
	current_date = datetime.date.today()
	print("	Welcome to Semicolon Expense Tracker App 	\n======================================== \n")

	while True:
		try:	
			choice = int(input("1. Add an expense \n2. View all expense \n3. Calculate total expenses \n4. Exit \n\nSelect an option: "))
		except ValueError:
				print("\nInvalid input... Enter only numerical value")
				continue
		match choice:
			case 1:
				date = input(f"Enter date (default:{current_date}): ")
				date = current_date
				add_date.append(date)
				description = input("Enter description: ")
				description = get_description(description)
				if description.startswith("invalid"):
					print(description)
					continue
				add_expense.append(description)
				amount = int(input("Enter amount: "))
				amount = get_amount(amount)
				add_amount.append(amount)
			case 2:		
				print(get_view_expenses(add_expense, add_date, add_amount))
			case 3:
				print(f"\nTotal Expenses is: {get_total_expenses(add_amount)} \n")
			case 4:
				print(get_exit())
				break
			case _:
				print("\nInvalid option... Kindly enter between 1 - 4")
main()