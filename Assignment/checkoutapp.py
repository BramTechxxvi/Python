class Checkoutapp:
	def main():
		pass

while True

	customername = input("Enter Customer's Name? ")
	item_bought = input("Enter Product Name? ")

	while True:
		try:
			item_quantity = int(input("\nHow many pieces? "))
			if item_quantity > 0:
				break
			else:
				print("Invalid input \nKindly enter again")
		except ValueError:
			print("Invalid input \nKindly enter again")

	while True:
		try:
			unit_price = int(input("\nHow much per unit? "))
			if unit_price > 0:
				break
			else:
				print("Invalid input \nKindly enter again")
		except ValueError:
			print("Invalid input \nKindly enter again")
	while True:
		addmoreitems = input("Would you like to add more items? ")
			if addmoreitems.lower == "NO"
				break
		
	

cashier_name = input("What is your name: ")

while True:
	try:
		discount = int(input("\nHow much discount will be given: "))
		if discount > 0 and discount <= 50:
			break
		else:
			print("Discount limit exceeded")
	except ValueError:
		print("Invalid input \nKindly enter again")

print(f"""
	SEMICOLON STORES
	MAIN BRANCH
	LOCATION: 312, HERBERT MACAULY WAY, SABO YABA, LAGOS.
	TEL: 03293828343
	DATE:
	Cashier: {cashier_name}
	Customer Name: {customername}
==========================================================================
ITEM			QTY		PRICE			TOTAL(NGN)



""")

