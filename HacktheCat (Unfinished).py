# Build a Program
# Hack the Cat: Hacking Into Cat Systems

# IMPORTING LIBRARIES
import random
import tabulate

# PRINTS GAME TITLE
print('\n\nHACK THE CAT\nby Atlas\n')

# PRINTS INTRODUCTION
def hackthecat():
    print('\nWelcome. You must be a lost traveller. ')
    print('You must have coincidentally found your way to our organisation. ')
    print('I am head of the clan. ')
    print('\nMy name is whatever you think it is. ')
    print('How I look is however you think I do. ')
hackthecat()

# PROMPTS USER TO ENTER NAME
def get_name():
    print('\n')
    name_input = input('What is your name, you intruder? \nName: ')
    return name_input
name_input = get_name()

# EXPLAINS ACTIVITY
def explain():
    print('\n\nWell, since you are here, {}, of course we won\'t let you off just like that. '.format(name_input))
    print('Whether you want to help us or not, it is a must. Unfortunately... it isn\'t a decision for you to make. ')
    print('\nWe are a hacking instituition: \nWe hack into the system of cats. ')
    print('\n"Hacking? Isn\'t that... ILLEGAL?"—you may say—Ha! Of course not. ')
    print('Laws we do not abide. ')
    print('\nFor you to have been brought here today is a matter of fate. \nAn invisible being leading you here to '
          'this world-saving corporation. ')
    print('\nWe thank you for coming here, {}! It is truly a blessing. '.format(name_input))
explain()