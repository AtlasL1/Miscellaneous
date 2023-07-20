# Python Basics
# Determine whether user input is palindrome (Word that reads the same backwards and forwards)

# LOWERCASE & REVERSING WORD(S)
def is_palindrome(word):
    # REMOVE ALL NON-ALPHANUMERIC CHARACTERS AND CONVERT TO LOWERCASE
    word = ''.join(e for e in word if e.isalnum()).lower()
    # CHECK IF THE STRING IS EQUAL TO REVERSE
    return word == word[::-1]

# RETRIEVE USER INPUT
word = input('\nEnter something: ')

# PRINT RESULTS
if is_palindrome(word):
    print('{} is a palindrome.'.format(word))
else:
    print('{} is not a palindrome.'.format(word))
