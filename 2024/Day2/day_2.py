f = open(file="2024/Day2/input.txt", mode="r")

ogInput = f.read()
newList = []

# get a proper list to work with
count = 0
temp =[]
temp2 = []
i = 0
while i < len(ogInput):
    if ogInput[i] == " ":
        temp2.append(ogInput[i-count:i])
        count = 0
    elif ogInput[i] == "\n":
        temp2.append(ogInput[i-count:i])
        newList.append(temp2[0:])
        temp2.clear()
        count = 0
    else :
        temp.append(ogInput[i])
        count += 1
    i+=1

# calculation for how many report are safe
# resolve part 1
unsafe = 0
unsafePart2 = 0
i = 0
while i < len(newList):
    internList = newList[i]
    allIncrease = False
    allDecrease = False
    levelGreater = False
    levelEqual = False
    y= 0
    while y < len(internList) -1:
        if int(internList[y]) < int(internList[y+1]):
            allIncrease = True
        if int(internList[y]) > int(internList[y+1]):
            allDecrease = True
        res = int(internList[y]) - int(internList[y+1])
        if res < -3 or res > 3:
            levelGreater = True
        if res == 0:
            levelEqual = True
        y += 1

    if allIncrease == True and allDecrease == True or levelGreater == True or levelEqual == True:
        unsafe += 1
    i+=1
print(unsafe)
safe = 1000 - unsafe
print(safe)

# resolve part 2
print(unsafePart2)
safePart2 = 1000 - unsafePart2
print(safePart2)
