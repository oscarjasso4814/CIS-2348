# Oscar Jasso
# PSID: 1895743

# accept input and initiate
word = input()
password = ''

# loop through input and replace letters with new characters
for letter in word:
    if letter == 'i':
        password += "!"
    elif letter == 'a':
        password += '@'
    elif letter == 'm':
        password += 'M'
    elif letter == 'B':
        password += '8'
    elif letter == 'o':
        password += '.'
    else:
        password += letter

# print new password with q*s added to end
print(f'{password}q*s')
