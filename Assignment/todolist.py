def display():
    return """
    1. Add task
    2. View all tasks
    3. Mark a task as completed
    4. Delete a task
    5. Exit
    """

def get_addtask(words):
    if not words.isalpha():
        return "Invalid input... Enter task again"
    if words.isnumeric():
        return "Invalid input..."
    return words

def get_viewtask(list1):
    if not list1:
        return "No task to view yet"
    for index in range(len(list1)):
        output = 'no                Task(s) \n'
        output+= f"{index +1}.    {[]} {list1[index]} \n"
    return output

def get_mark():
    pass

def get_delete(list1):
    return 'Deleted successfully'

def get_exit():
    return "Thanks For Using To-Do List Manager"

def main():
    addtasks = []
    print("     To-Do List Manager \n ")

    while True:
        print(display())
        try:
            choice = int(input("Select an option: "))
        except ValueError:
            print("\nInvalid input... Enter again")
            continue
        match choice:
            case 1:
                addtask = input("\nAdd a task: ")
                addtask = get_addtask(addtask)
                if addtask.startswith("Invalid"):
                    continue
                addtasks.append(addtask)
            case 2:
                print(get_viewtask(addtasks))
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