from tkinter.font import names

file = open("demo.txt", 'w')

for index in range(1, 11):
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    file.write(f"{index}   {name}   {age}\n")


file.close()

with open("demo.txt", 'r') as file2:
    names = file2.read()
    print(names)

