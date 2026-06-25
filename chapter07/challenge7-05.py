number1 = [8,19,148,4]
number2 = [9,1,33,83]
li = []
for a in range(len(number1)):
    for b in range(len(number2)):
            li.append(number1[a]*number2[b])

print(li)
