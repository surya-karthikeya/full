# METHOD-2 using set

input_list = str(input("Enter elements separated by Comma ")).split(",")

for z in range(0, len(input_list)):
    input_list[z] = int(input_list[z])

print("The original List:",input_list)

temp = set(input_list)
no_duplicates = list(temp)

print("The list with no duplicates:",sorted(no_duplicates))

