
response = raw_input(
"What operation would you like to perform? (please type (a)dd, (s)ubtract, (m)ultiply, (d)ivide, (q)uit. "
)

while response != "q":
    if response == "a":
        number1 = raw_input(
            "What is the first number you would like to add? "
        )
        number2 = raw_input(
            "What is the second number you would like to add? "
        )

        answer = float(number1) + float(number2)
        print answer
        response = raw_input(
            "What operation would you like to perform? (type (a)dd, (s)ubtract, (m)ultiply, (d)ivide, (q)uit) "
        )
    elif response == "s":
        number1 = raw_input(
            "What is the first number you would like to subtract? "
        )
        number2 = raw_input(
            "What is the second number you would like to subtract? "
        )

        answer = float(number1) - float(number2)
        print answer
        response = raw_input(
            "What operation would you like to perform? (type (a)dd, (s)ubtract, (m)ultiply, (d)ivide, (q)uit) "
        )
    elif response == "m":
        number1 = raw_input(
            "What is the first number you would like to multiply? "
        )
        number2 = raw_input(
            "What is the second number you would like to multiply? "
        )

        answer = float(number1) * float(number2)
        print answer
        response = raw_input(
            "What operation would you like to perform? (type (a)dd, (s)ubtract, (m)ultiply, (d)ivide, (q)uit) "
        )
    elif response == "d":
        number1 = raw_input(
            "What is the first number you would like to divide? "
        )
        number2 = raw_input(
            "What is the second number you would like to divide? "
        )

        answer = float(number1) / float(number2)
        print answer
        response = raw_input(
            "What operation would you like to perform? (type (a)dd, (s)ubtract, (m)ultiply, (d)ivide, (q)uit) "
        )
    else:
        print "Sorry, didn't understand your response. Try again."
        response = raw_input(
            "What operation would you like to perform? (type (a)dd, (s)ubtract,(m)ultiply, (d)ivide, (q)uit) "
        )

print "Thanks for using the calculator!"
