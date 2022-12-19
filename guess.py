import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}:'))
        if guess > random_number:
            print ('its high')
        elif guess < random_number:
            print ('its low')
        else:
            print (f'afarin 100 afarin adade dorost {guess}')
    #print (f'afarin 100 afarin adade dorost {guess} bood')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (l), or correct(C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'I Guessed it, you are so predictable, I knew it was {guess} 😏 ')

computer_guess(100)