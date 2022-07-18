#Akinola Daramola Jr
#Programming Exercise 3.3
#Due Date: 06/23/2022



"""
Write a program that asks the user to enter a person’s age. The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult. Following are the guidelines:

If the person is 1 year old or less, he or she is an infant.

If the person is older than 1 year, but younger than 13 years, he or she is a child.

If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.

If the person is at least 20 years old, he or she is an adult.

"""

#Initializing age variable
age = 0

#Declaring value of age
age = int(input("Enter age of person: "))

#Conditional Statement
if age >= 20:
    print('This person is an adult.')
elif age >= 13 and age < 20:
    print("This person is a teenager.")
elif age > 1 and age < 13:
    print("This person is a child.")
else:
    print("This person is an infant.")
    
