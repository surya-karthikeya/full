# METHOD-1

input_list = str(input("Enter elements separated by Comma ")).split(",")

for z in range(0,len(input_list)):
    input_list[z]=int(input_list[z])

print("The original List:", input_list)
no_duplicates = []

for i in input_list:
    if i not in no_duplicates:
        no_duplicates.append(i)

print("The list with no duplicates:",no_duplicates)
