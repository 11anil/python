exp = [2000, 3000, 3000, 4000]
# Total = 0
# for item in exp:
#     Total = Total + item
#     print(Total)

# range function
total = 0
for i in range(len(exp)):
    print('month:', (i+1), 'expense:', exp[i])
    total = total + exp[i]
    print('total expense is :',total)

