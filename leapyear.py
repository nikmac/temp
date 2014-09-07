def leap_year_calc():
    what_year = raw_input("What year would you like to check?  ")
    what_year = int(what_year)

    if what_year % 4 == 0 and what_year % 100 != 0:
        print "{} is a leap year. ".format(what_year)
    else:
        print "{} is not a leap year. ".format(what_year)
    leap_year_calc()

leap_year_calc()
