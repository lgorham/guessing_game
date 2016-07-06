# Put your code here
import random

name = raw_input("What is your name? ")
random_int = random.randint(1,100)
guess = int(raw_input("Hello %s Pick an integer between 1 and 100: " % name))
previous_guesses = []
#print random_int

while guess != random_int:
    if guess < random_int:
        print "Guess is too low, try again"
    elif guess > random_int:
        print "Guess is too high, try again"
    previous_guesses.append(guess)
    guess = int(raw_input("Enter a new guess: "))

print "You guessed it %s! It took you %s tries" % (name, len(previous_guesses))


