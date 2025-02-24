total = 0

while True:
	try:
		menu = int(input("1. Deposit \n2. Withdraw \n3. Exit \n\nSelect an option:  " ))
	except ValueError:
		print("Invalid input... Enter option again \n")
		continue
	match menu:
		case 1:
			while True:
				try:
					deposit = float(input("Enter deposit Amount: "))
					if deposit <= 0:
						print("Invalid input... Enter positive values \n")
					else:
						total += deposit
						print(f"Deposit Succesful \nYour present balance is: {total}")
						break
				except ValueError:
					print("Invalid input... try again \n")
		case 2: 
			while True:
				try:
					withdraw = float(input("Enter withdrawal Amount: ")) 
					if withdraw <= 0:
						print("Invalid input... Enter positive value \n")
						continue
					if withdraw > total:
						print("Insufficient funds")
					else:
						total -= withdraw
						print(f"Withdrawal Succesful... Your new balance is: {total} \n")
				except ValueError:
					print("Invalid input...")
		case 3:
			print("THANK YOU!")
			break 
	    
		case _:
			print("\n\nInvalid option... Enter number between 1-4 \n")

	