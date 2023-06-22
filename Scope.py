# Variable scope in python

# A Variable scope is only available from inside the region it is created

# global sxope = variable available from within any scope

# local variable = variable created inside function

calculate_to_hours = 24
name_of_unit = "hours"

# def days_to_units(num_of_days, custom_message):
#     print(f"{num_of_days} days have {num_of_days * calculate_to_hours} {name_of_unit}")
#     print(custom_message)

# days_to_units(35, "Awesome")
# days_to_units(50, "Fantastic")
# days_to_units(60, "Great")
# days_to_units(20, "Excellent")

def scope_check():
    my_var = "variable inside function"
    print(name_of_unit)  # global variable accessible
    print(my_var)

scope_check()
