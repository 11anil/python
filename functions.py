calculate_to_hours = 24 
name_of_unit = "hours"


# def days_to_units():

#     print(f"20 days have {20 *calculate_to_minutes } {name_of_unit}")
#     print(f"35 days have {35 * calculate_to_minutes } {name_of_unit}")
#     print("All Good")


# days_to_units()


# Function arguments

def days_to_units(num_of_days,custom_message):

    print(f"{num_of_days} days are have {num_of_days * calculate_to_hours} {name_of_unit}")
    print(custom_message)
days_to_units(35,"Awesome")
# days_to_units(50)
# days_to_units(60)
# days_to_units(20)
print("All good")

# f stands for format
# after defining arguments you must have to define the value in the parameter otherwise you must face an error