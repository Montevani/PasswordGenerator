import random

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890}{)(][#:;^,.?!|&_~@$%\/=-+*"'
print('- Password Generator -')
number = int(input('How many passwords do you want to generate? '))
length = int(input('How many characters do you want on your password? '))
print('\nHere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)