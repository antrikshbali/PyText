#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
#! FirstName M. LastName
first_name = str(input("Please enter your first name: "))
middle_name = str(input("Please enter your middle name: "))
last_name = str(input("Please enter your last name: "))

first_name = first_name.capitalize()
middle_name = middle_name.capitalize()
last_name = last_name.capitalize()

name_format = "{first} {middle:.1s} {last}" #! s -> converts to string
print(name_format.format(first=first_name,middle=middle_name,last=last_name))
