import random

number = random.randint(1, 100)
player = input("Hello, what's your name?")
guess_attepmts = 0

print('Okay! '+ player + ' I am guessing a number between 1 and 100:')

while guess_attepmts < 5:
    guess = int(input())
    guess_attepmts += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break

if guess == number:
    print('You guessed the number in ' + str(guess_attepmts) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))
