amountperparcel = 0
basepay = 5000

collectionrate = int(input("Enter successful delivery: "))

if collectionrate < 50:
	amountperparcel = 160
elif collectionrate <= 59:
	amountperparcel = 200
elif collectionrate <= 69:
	amountperparcel = 250
elif collectionrate >= 70:
	amountperparcel = 500

riderswage = (collectionrate * amountperparcel) + basepay
print(f"Rider's Wage = {riderswage}")