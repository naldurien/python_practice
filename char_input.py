# From practicepython.org - "CHARACTER INPUT"

# Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that 
#they will turn 100 years old.

#Extras:
# Ask the user for another number and printing out that many copies of the
# previous message.
# Print out that many copies of the previous message on separate lines.

def one_hundred():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    birthday = input("Has your birthday occurred yet this year? Y/N: ")
    random = int(input("Please enter a number between 1 and 10: "))
    year = (100 - age) + 2021
    if birthday == "y":
       for index in range(random):
            print(f"{name}, you will turn 100 years old in the year {year}.")
    elif birthday == "n":
       for index in range(random):
            print(f"{name}, you will turn 100 years old in the year {year - 1}.")

one_hundred()
