# Ask the user for a number. Depending on whether the number is even or odd, i
# print out an appropriate message to the user. 

# If the number is a multiple of 4, print out a different message.

# Ask the user for two numbers: one number to check (call it num) and one number# to divide by (check). If check divides evenly into num, tell that to the user.# If not, print a different appropriate message.

def even_odd(num):
    if num % 2 == 0:
        print("Your number is even.")
    if num % 4 == 0:
        print("Your even number is also divisible by 4.")
    else:
        print("Your number is odd.")


def divisible(num, divisor):
    if num % divisor == 0:
        print("Your number is evenly divisible by your divisor.")
    else: 
        print("Your number is not evenly divisible by your divisor.")

