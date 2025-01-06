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

numberofguest = int(input("Number Of Guest: "))

pizzatype = input("""
		Enter Preferred Pizza Type: 
		
		 Sapa size
		 Small money
		 Big boys
		 Odogwu

""").strip().lower()

slicesperbox = 0
priceperbox = 0


if pizzatype.lower() == "sapa size":
	slicesperbox = 4
	priceperbox = 2500

elif pizzatype.lower() == "small money":
	slicesperbox = 6
	priceperbox = 2900

elif pizzatype.lower() == "big boys":
	slicesperbox = 8
	priceperbox = 4000

elif pizzatype.lower() == "odogwu":
	slicesperbox = 12
	priceperbox = 5200

else:
	print("invalid order \nKindly enter order again.")

boxesneeded = (numberofguest + slicesperbox - 1) // slicesperbox
totalslices = boxesneeded * slicesperbox
leftoverslices = totalslices - numberofguest
totalprice = boxesneeded * priceperbox
print(f""" 
	Number of box(es) to buy = {boxesneeded} box(es). 
	{pizzatype} size contains {slicesperbox} slices per box.
	{boxesneeded} box(es) should be sufficient for {numberofguest} peron(s) as it would contain {totalslices} in all.
	Number of left over slices after serving = {leftoverslices} slice(s).
	Price = {totalprice}
	""")

