# Put your code here
import random

def is_int(guess):
    """"evaluates if input is integer in range"""
    try:
        int_guess = int(guess)
        print int_guess
    except: 
        # if it's not a string of an integer (letters, float, etc)
        return False
    # will only get here if try clause works
    if int_guess <= 100 and int_guess >= 1:
        return True
    else:
        return False
 

def guess_game(name, random_int):
    """"evaluates if user guess matches random integer"""
    guess = 0
    previous_guesses = []
    while guess != random_int:
        guess = raw_input("%s, enter a guess between 1 - 100: " % name)
        evaluate_input = is_int(guess)
        if evaluate_input == True:
            guess = int(guess)
            if guess < random_int:
                print "Guess is too low, try again"
            elif guess > random_int:
                print "Guess is too high, try again"
        else:
            print "That is not a valid integer between 1-100:"
        previous_guesses.append(guess)

    print "You guessed it %s! It took you %s tries" % (name, len(previous_guesses))
    number_of_tries = len(previous_guesses)
    return number_of_tries

def play_game(name):
    answer = "Y"
    low_num_tries = 500
    high_num_tries = 0
    while answer == 'Y':
        comp_random = random.randint(1,100)
        print comp_random
        current_round = guess_game(name, comp_random)
        if current_round > high_num_tries:
            high_num_tries = current_round
        if current_round < low_num_tries:
            low_num_tries = current_round
        answer = raw_input("Do you want to play the game? Y or N: ")
    print "Good-bye!, your worst score was: %s and your best score was: %s" % (high_num_tries, low_num_tries)


user_name = raw_input("What is your name? ")
play_game(user_name)




    # guess = raw_input("Hello %s Pick an integer between 1 and 100: " % name)
    # previous_guesses = []
    # while guess != random_int:
    #     evaluate_input = is_int(guess)
    #     print "evaluate input", evaluate_input
    #     if evaluate_input == True:
    #         guess = int(guess)
    #         if guess < random_int:
    #             print "Guess is too low, try again"
    #         elif guess > random_int:
    #             print "Guess is too high, try again"
    #         previous_guesses.append(guess)
    #     else:
    #         print "That is not a valid number between 1-100:"
    #         # guessGame(name, random_int)
    #     guess = raw_input("Enter a new guess: ")
    # print "You guessed it %s! It took you %s tries" % (name, len(previous_guesses))

