def calculator():
    print "Welcome to the Calculator"
    user_choice = raw_input("Do you want to add(+) or subtract(-)?")

    if user_choice == "+":
        number1 = raw_input("Great, please enter the first number you would like to {}: ".format(user_choice))
        number1 = float(number1)
        number2 = raw_input("And the second: ")
        number2 = float(number2)
        answer = number1 + number2
        print "{} + {} = {}".format(number1, number2, answer)

    elif user_choice == "-":
        number1 = raw_input("Great, please enter the first number you would like to {}: ".format(user_choice))
        number1 = float(number1)
        number2 = raw_input("And the second: ")
        number2 = float(number2)
        answer = number1 - number2
        print "{} - {} = {}".format(number1, number2, answer)

    else:
        print "Oops, try again. You must enter + or - to begin."
        calculator()

calculator()