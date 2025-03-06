f = open(file="2024/input.txt", mode="r")

OGlist = f.read()
newList1 = []
newList2 = []

max = 5
i= 0
while i < len(OGlist):
    if OGlist[i] == ' ':
        newList1.append(OGlist[i-5:i])
        i += 2
    if OGlist[i] == '\n':
        newList2.append(OGlist[i-5:i])
    i += 1

newList1.sort()
newList2.sort()

# response for the first part 
finalResponse = 0
newI = 0
while newI < len(newList1):
    if int(newList1[newI]) > int(newList2[newI]):
        finalResponse += int(newList1[newI]) - int(newList2[newI])
    if int(newList2[newI]) > int(newList1[newI]):
        finalResponse += int(newList2[newI]) - int(newList1[newI])
    newI += 1

print(finalResponse)

# Response for the second part 
finalSimilarity = 0
occurence = 0
a = 0 
b = 0
while a < len(newList1):
    while b < len(newList2):
        if newList1[a] == newList2[b]:
            occurence += 1
        b += 1
    finalSimilarity = int(newList1[a]) * occurence + finalSimilarity
    occurence = 0
    b = 0
    a += 1
print(finalSimilarity)