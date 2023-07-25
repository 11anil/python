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

def excecute_and_validate():
    if user_input.isdigit():
      user_input_number = int(user_input)
      calculated_value = days_to_units(user_input_number)
      print(calculated_value)
    else:
        print("you entered a non-integer value , plz provide a integer value")


        user_input = input("hey user enter a number -\n")
   
# print(type("this should be a type of string"))
 