import random

shirts = ["pink", "stripes", "giants", "long sleeve", "yellow"]
already_worn = []
closet = len(shirts)

def choose():
    choose_shirt = random.randint(0, (closet-1))
    chosen_shirt = shirts[choose_shirt]
    return chosen_shirt

def worn(chosen_shirt):
    already_worn.append(chosen_shirt)
    shirts.remove(chosen_shirt)
    print "Lookin sharp"

def shirt_shuffle():
    for shirt in shirts:
        chosen_shirt = choose()
        wear = raw_input("Today's shirt is {}.  Do you want to wear this? (y/n) ".format(chosen_shirt))
        if wear == "y":
            worn(chosen_shirt)
            return len(shirts)
        elif wear == "n":
            chosen_shirt = choose()
            another_choice = raw_input("Maybe you would prefer: {} (y/n)".format(chosen_shirt))
            if another_choice == "y":
                worn(chosen_shirt)
                return len(shirts)
            if another_choice == "n":
                print "staying on the couch today?"
                return len(shirts)
        else:
            print "please enter a valid answer."


while closet >= 0:
    if closet == 0:
        print "Laundry time"
    closet = shirt_shuffle()



