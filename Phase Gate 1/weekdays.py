weekdays_list = [0] * 7
while True:
	try:
		day_of_the_week = int(input("Enter todays day 0-6: "))
		if day_of_the_week < 0 or day_of_the_week > 6:
			print("Invalid Input")
		else:
			break
	except ValueError:
		print("Invalid Input")
if day_of_the_week == 0:
	weekdays_list[0] = "Sunday"

elif day_of_the_week == 1:
	weekdays_list[1] = "Monday"

elif day_of_the_week == 2:
	weekdays_list[2] = "Tuesday"

elif day_of_the_week == 3:
	weekdays_list[3] = "Wednesday"

elif day_of_the_week == 4:
	weekdays_list[4] = "Thursday"

elif day_of_the_week == 5:
	weekdays_list[5] = "Friday"

elif day_of_the_week == 6:
	weekdays_list[6] = "Saturday"

print(f"{weekdays_list}")
	
