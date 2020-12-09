import random
import string

length = 0
while length < 6:
    length = int(input('How long is your password? '))
    if length < 6:
        print('Must be at least 6! ')

numLetters = length+1
while numLetters > length or numLetters < 0:
    numLetters = int(input('Number of letters? '))
    if numLetters > length:
        print(f'Must be less than {length}!')
    if numLetters < 0:
        print('Must not be negative!')

numNumbers = length+1
while numNumbers > length-numLetters or numNumbers < 0:
    numNumbers = int(input('Number of numbers? '))
    if numNumbers > length-numLetters:
        print(f'Must be less than {length-numLetters}!')
    if numNumbers < 0:
        print('Must not be negative!')

pword_parts = ''.join(random.choice(string.ascii_letters) for i in range(numLetters))
pword_parts += ''.join(random.choice(string.digits) for i in range(numNumbers))
pword_parts += ''.join(random.choice(string.punctuation) for i in range(length-numLetters-numNumbers))

pword_list = list(pword_parts)
random.shuffle(pword_list)
pword_final = ''.join(pword_list)

print(f'Your password is: {pword_final}')