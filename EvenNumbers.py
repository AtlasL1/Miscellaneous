# Python Basics
# Retrieve only even numbers from user input of random numbers

def is_even(num):
    # CHECK IF THE NUMBER IS DIVISIBLE BY 2
    return num % 2 == 0

# PROMPT THE USER TO ENTER LIST NUMBERS
num_list = input("\nEnter a list of numbers and separate them by commas: ").split(",")

# CONVERT THE INPUT LIST TO INTEGERS
num_list = [int(num) for num in num_list]

# PRINT OUT ONLY EVEN NUMBERS FROM USER INPUT
even_list = [num for num in num_list if is_even(num)]
print("\nEven numbers found:", even_list)