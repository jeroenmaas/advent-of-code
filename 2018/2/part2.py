from utils.utils import file_get_contents

file = file_get_contents('input.txt')

lines = file.splitlines()

for line1 in lines:
    for line2 in lines:

        differences = 0
        x = []
        newLine = ""
        for i in range(len(line2)):
            letter1 = line1[i]
            letter2 = line2[i]

            if letter1 != letter2:
                x.append([letter1, letter2])
                differences += 1
            else:
                newLine += letter1

        if differences == 1:
            print(line1)
            print(line2)
            print(x)
            print("Result to copy: " + newLine)
            exit()