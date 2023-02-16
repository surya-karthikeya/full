# Problem 2-Making tuple pairs of a list

def pair(sample_list):
    result = [
        (sample_list[i], sample_list[len(sample_list) - i - 1])
        for i in range(len(sample_list) // 2)
    ]
    return result

sample_list = str(input("Enter elements separated by Comma ")).split(",")

for z in range(0,len(sample_list)):
    sample_list[z] = int(sample_list[z])

print("The pairs of tuples are: ", pair(sample_list))
