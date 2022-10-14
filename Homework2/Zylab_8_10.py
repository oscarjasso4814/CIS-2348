# Oscar Jasso
# PSID: 1895743

# create function that removes spaces from the input given.
# compare the reverse of the word with no spaces to the word with no spaces
# if they are the same print out a confirmation, do the same for the opposite
def is_palindrome(word):
    no_space_word = word.replace(' ', '')

    if no_space_word[::-1] == no_space_word:
        print(f'{word} is a palindrome')
    else:
        print(f'{word} is not a palindrome')

# ask for user input
# call function with user input


user_input = input()
is_palindrome(user_input)
