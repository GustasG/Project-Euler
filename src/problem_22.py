def getNames(file_name):
    with open(file_name, "r") as f:
        list = f.readline().split(",")


    for i in range(0, len(list)):
        list[i] = list[i].strip('"')

    list.sort()

    return list


def calculateASCII(name):
    sum = 0

    for letter in name:
        sum += ord(letter) - 64

    return sum


names = getNames("problem_22_names.txt")
sum = 0

for i in range(len(names)):
    sum += (i + 1) * calculateASCII(names[i])

print(sum)
