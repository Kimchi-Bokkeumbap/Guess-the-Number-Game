#This is a guess the number game.
import random

print('Hi, Welcome to Guess The Number game. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 50. You have 10 tries to guess my number')
randomNumber = random.randint(1,50)

for guessesTaken in range(1,11):
	print('Take a guess.')
	guess = int(input())

	if guess < randomNumber:
		print('Your guess is too low')
	elif guess > randomNumber:
		print('Your guess is too high.')
	else:
		break #This condition is for the correct guess!

if guess == randomNumber:
	print('You guessed it ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
	print('Sorry. The number I was thinking of was ' + str(randomNumber))

print('You took ' + str(guessesTaken) + ' guesses.')
