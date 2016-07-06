# Put your code here
import random

def isInt(guess):
    try:
        int_guess = int(str_guess)
        return True
    except:
        return False

    # return type(guess) is int
 
def guessGame(name, random_int):
    str_guess = raw_input("Hello %s Pick an integer between 1 and 100: " % name)
    evaluate_input = isInt(str_guess)
    if evaluate_input == True:
        previous_guesses = []
        while guess != random_int:
            if guess < random_int:
                print "Guess is too low, try again"
            elif guess > random_int:
                print "Guess is too high, try again"
            previous_guesses.append(guess)
            guess = int(raw_input("Enter a new guess: "))
    else:
        print "That is not a valid number between 1-100:"
        # guessGame(name, random_int)

    print "You guessed it %s! It took you %s tries" % (name, histlen(previous_guesses))


user_name = raw_input("What is your name? ")
random = random.randint(1,100)
guessGame(user_name, random)