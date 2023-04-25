# num = input("Enter a Number :")
# num = int(num)
# if num % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")


indian = ["samosa", "biryani"]
chinese = ["chillie potato", "chowmein"]
italian = ["pizza", "pasta"]

dish = input("Eneter a dish name :")

if dish in indian:
    print("indian")
elif dish in italian:
    print("dish is italian")
elif dish in chinese:
    print("dish is chinese")
else:
    print("i just dont know which type of dish is this")
