calculation_to_units = 24
name_of_unit = "hours"



def days_to_units(num_of_days):
    condition_check = num_of_days > 0
    print(type(condition_check))
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days* calculation_to_units} {name_of_unit}"

    elif num_of_days == 0:
        return ("you entered zero value")
    # else:
    #     return "you entered a negative value , no calculation for you!"

user_input = input("hey user enter a number and will convert it in hours -\n")


def excecute_and_validate():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)
    else:
        print("you entered a non-integer value , plz provide a integer value")

excecute_and_validate()
        
# print(type("this should be a type of string"))
