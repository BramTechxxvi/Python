def display():
	return """
	1. Add task
	2. View all tasks
	3. Mark a task as completed
	4. Delete a task
	5. Exit
	"""

def get_add_task(words):
	if not words.isalpha:
		return "Invalid input... Enter task again"
	if words.isnumeric():
		return "Invalid input..."
	return words

def get_view_task(list1):
	if not list1:
		return "No task to view yet"
	for index in range(len(list1)):
		output = 'no                Task(s) \n'
		output += f"{index +1}.    {[]} {list1[index]} \n"
	return output

def get_mark():
	pass

def get_delete():
	return 'Deleted successfully'


def get_exit():
	return "Thanks For Using To-Do List Manager"

def main():
	add_task_list = []
	print("========== To-Do List Manager ==========\n")
	while True:
		print(display())
		try:
			choice = int(input("Select an option: "))
		except ValueError:
			print("\nInvalid input... Enter again")
			continue
		match choice:
			case 1:
				add_task = input("\nAdd a task: ")
				add_task = get_add_task(add_task)
				print("Task added successfully.")
				add_task_list.append(add_task)
			case 2:
				print(get_view_task(add_task_list))
			case 3:
				print(get_mark())
			case 4:
				print(get_delete())
			case 5:
				print(get_exit())
				break
			case _:
				print("\nInvalid option... Kindly enter between 1 - 5")
main()