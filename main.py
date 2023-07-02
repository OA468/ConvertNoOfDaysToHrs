from helper import validate_and_execute

#from helper import validate_and_execute

user_input = ""

while user_input != "exit":

    user_input = input("Hey user, enter number of days  & unit to convert the value to !\n")
    # "user_input" variable to accept user input

    days_and_units = user_input.split(":")

    days_and_unit_dictionary = {"days": days_and_units[0], "unit": days_and_units[1]}

    validate_and_execute(days_and_unit_dictionary)




