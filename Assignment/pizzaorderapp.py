import math
print("""
		<<<WELCOME TO IYA MOSES PIZZA Joint>>> 

		Kindly Place An Order From Our Menu Below

		__________________________________________________
                |  Pizza Type   | Slices Per Box  | Price Per Box|
		|_______________|_________________|______________|
		| Sapa Size	|	4	  |   2,500      |
		|_______________|_________________|______________|
		| Small Money	|	6	  |   2,900      |
		|_______________|_________________|______________|
		| Big Boys	|	8	  |   4,000      |
		|_______________|_________________|______________|
		| Odogwu 	|       12	  |   5,200      |
		|_______________|_________________|______________|

""")
while True:
	try:
		numberofguest = int(input("Number Of Guest: "))
		if numberofguest > 0:
			break
		else:
			print("invalid Input \nKindly enter again")
	except ValueError:
		print("Invalid Input \n Kindly enter again")
pizzatype = input("""
		Enter Preferred Pizza Type: 
		
		 Sapa size
		 Small money
		 Big boys
		 Odogwu

""").strip().lower()

if pizzatype.lower() == "sapa size":
	slicesperbox = 4
	priceperbox = 2500

elif pizzatype.lower() == "small money":
	slicesplowererbox = 6
	priceperbox = 2900

elif pizzatype.lower() == "big boys":
	slicesperbox = 8
	priceperbox = 4000

elif pizzatype.lower() == "odogwu":
	slicesperbox = 12
	priceperbox = 5200

else:
	print("invalid order \nKindly enter order again.")

boxesneeded = math.ceil(numberofguest / slicesperbox)
totalslices = boxesneeded * slicesperbox
leftoverslices = totalslices - numberofguest
totalprice = boxesneeded * priceperbox
print(f""" 
	Number of box(es) to buy = {boxesneeded} box(es). 
	{pizzatype} size contains {slicesperbox} slices per box.
	{boxesneeded} box(es) should be sufficient for {numberofguest} persson(s) as it would contain {totalslices} in all.
	Number of left over slices after serving = {leftoverslices} slice(s).
	Price = {totalprice}
	""")