def temperature_converter():
    temperature = raw_input("Please input the temperature you are starting with: ")
    temperature = float(temperature)
    conversion = raw_input("Would you like to convert this to (F)ahrenheit or (C)elsius? ").lower()
    if conversion == "f":
        temperature_verbose = "{} C".format(temperature)
        answer = (9.0/5.0) * temperature + 32
        answer_verbose = "{} F".format(answer)

    elif conversion == "c":
        temperature_verbose = "{} F".format(temperature)
        answer = (5.0/9.0) * (temperature - 32)
        answer_verbose = "{} C".format(answer)

    else:
        print "Please follow the prompts and input either 'f' or 'c' for temperature conversion."
        temperature_converter()

    print "{} = {}".format(temperature_verbose, answer_verbose)
    temperature_converter()

temperature_converter()
