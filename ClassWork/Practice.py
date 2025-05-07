import re

def get_result(name):
    if re.match(r'\d+ [A-Z][a-z]* [A-Z][a-z]*', name):
        return name
    else:
        return "Hello "

def verify_password(name):
    if re.match(r'[\dA-Za-z_.]+@[a-zA-Z0-9]+.[a-zA-Z0-9]', name):
        return name
    else:
        return "Hello "


check = input("Enter: ")
print(verify_password(check))
