from random import *

correct = 0


def q_length():
    quiz_length = raw_input("How many questions would you like to answer?  ")
    quiz_length = int(quiz_length)
    return quiz_length


def q_type(question_count, chosen_level ):
    question_type = raw_input("What type of questions would you like? (a)ddition, (s)ubtraction, (m)ultiplication, (d)ivision, or mi(x)ed  ").lower()
    for question in question_type:
        if question == "a":
            addition(question_count, chosen_level)
            return
        elif question == "s":
            subtraction(question_count, chosen_level)
            return
        elif question == "m":
            multiplication(question_count, chosen_level)
            return
        elif question == "d":
            division(question_count, chosen_level)
            return
        elif question == "x":
            mixed(question_count, chosen_level)
            return
        else:
            print "sorry, didn't catch that."
            q_type(question_count, chosen_level)


def user_level():
    levels = raw_input("Are you a (b)eginner, (i)ntermediate, or (a)dvanced?  ").lower()
    return levels


def get_numbers(levels):
    if levels == "b":
        start_range = randint(1, 10)
        end_range = randint(1, 10)
    elif levels == "i":
        start_range = randint(1, 25)
        end_range = randint(1, 25)
    elif levels == "a":
        start_range = randint(1, 100)
        end_range = randint(1, 100)
    else:
        print "sorry, didn't catch that."

    return start_range, end_range


def addition(question_count, chosen_level):
    global correct
    for i in range(0, question_count):
        start_range, end_range = get_numbers(chosen_level)
        prod = start_range + end_range
        ans = input("What's %d plus %d? " % (start_range, end_range))
        if ans == prod:
            print "That's right -- well done.\n"
            correct += 1
        else:
            print "No, I'm afraid the answer is %d.\n" % prod
    return int(correct)


def subtraction(question_count, chosen_level):
    global correct
    for i in range(0, question_count):
        start_range, end_range = get_numbers(chosen_level)
        prod = start_range - end_range
        ans = input("What's %d minus %d? " % (start_range, end_range))
        if ans == prod:
            print "That's right -- well done.\n"
            correct += 1
        else:
            print "No, I'm afraid the answer is %d.\n" % prod
    return int(correct)


def multiplication(question_count, chosen_level):
    global correct
    for i in range(0, question_count):
        start_range, end_range = get_numbers(chosen_level)
        prod = start_range * end_range
        ans = input("What's %d times %d? " % (start_range, end_range))
        if ans == prod:
            print "That's right -- well done.\n"
            correct += 1
        else:
            print "No, I'm afraid the answer is %d.\n" % prod
    return int(correct)


def division(question_count, chosen_level):
    global correct
    for i in range(0, question_count):
        start_range, end_range = get_numbers(chosen_level)
        prod = start_range / end_range
        ans = input("What's %d divided by %d? " % (start_range, end_range))
        if ans == prod:
            print "That's right -- well done.\n"
            correct += 1
        else:
            print "No, I'm afraid the answer is %d.\n" % prod
    return int(correct)


def mixed(question_count, chosen_level):
    for q in range(question_count):
        mixed_question = randint(1, 4)
        if mixed_question == 1:
            addition(1, chosen_level)
        elif mixed_question == 2:
            subtraction(1,chosen_level)
        elif mixed_question == 3:
            multiplication(1, chosen_level)
        elif mixed_question == 4:
            division(1, chosen_level)
        else:
            print "Ack!"


def score(question_count):
    print "in score method"
    global correct
    fraction_correct = correct/question_count
    two_thirds = float(2)/float(3)
    print(two_thirds)
    one_third = float(1)/float(3)
    print "\nI asked you {} questions.  You got %d of them right.".format(question_count) % correct
    if float(fraction_correct) >= two_thirds:
        print "Well done!"
        print ""
    elif (float(fraction_correct) < two_thirds) and (float(fraction_correct) > one_third):
        print "You need more practice"
        print ""
    elif float(fraction_correct) < one_third:
        print "Please ask your teacher for help!"
        print ""
    else:
        print "cool"


def math_quiz():
    print ""
    print "Welcome to Math Quiz!"
    print ""
    question_count = q_length()
    chosen_level = user_level()
    q_type(question_count, chosen_level )
    score(question_count)


math_quiz()



