from random import randint

def guessing_game():
    print "Time to play the guessing game!"
    print ""
    computer = randint(1, 100)
    count = 0
    user_guess = None
    while user_guess != computer:
        user_guess = raw_input("Please enter a guess between 1 and 100:  ")
        user_guess = int(user_guess)

        if user_guess < computer:
            print "{} is too low, try again: ".format(user_guess)
            count += 1

        elif user_guess > computer:
            print "{} is too high, try again: ".format(user_guess)
            count += 1

        else:
            count += 1
            print "Congratulations!  {} is the correct guess. You got it in {} tries. ".format(user_guess, count)


guessing_game()