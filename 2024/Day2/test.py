f = open(file="2024/Day2/input.txt", mode="r")

ogInput = f.read()
newList = []

# get a proper list to work with
count = 0
temp = []
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
    else:
        temp.append(ogInput[i])
        count += 1
    i += 1

# calculation for how many reports are safe
unsafe = 0
i = 0
while i < len(newList):
    internList = newList[i]
    allIncrease = True
    allDecrease = True
    levelGreater = False
    levelEqual = False
    y = 0
    while y < len(internList) - 1:
        if int(internList[y]) < int(internList[y + 1]):
            allDecrease = False
        if int(internList[y]) > int(internList[y + 1]):
            allIncrease = False
        res = int(internList[y]) - int(internList[y + 1])
        if res < -3 or res > 3:
            levelGreater = True
        if res == 0:
            levelEqual = True
        y += 1
    if not allIncrease and not allDecrease or levelGreater or levelEqual:
        unsafe += 1
    i += 1

print(unsafe)
safe = 1000 - unsafe
print(safe)