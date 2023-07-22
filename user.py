calculate_to_units = 24
name_of_unit = "hours"

def day_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days* calculate_to_units} {name_of_unit}"

# my_var = day_to_units(20)
# print(my_var)

user_input = input("hey user, enter a num of days and i will convert it to hours!\n")
user_input_number = int(user_input)
calculated_value = day_to_units(user_input_number)
print(calculated_value)
