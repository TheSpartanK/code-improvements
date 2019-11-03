import random

# This takes a list of 4 items and randomly reorders it based on pos0 worth 8, pos1 worth 4, pos2 worth 2 and pos3 worth 1

def randomWeightedSort(theList):

    newOrder = []

    n = random.randint(1, 15)

    if n >= 1 and n <= 8:
        newOrder.append(theList[0])  # 0
        m = random.randint(1, 7)
        if m >= 1 and m <= 4:
            newOrder.append(theList[1])  # 0,1
            o = random.randint(1, 3)
            if o >= 1 and o <= 2:
                newOrder.append(theList[2])  # 0,1,2
                newOrder.append(theList[3])  # 0,1,2,3
            elif o == 3:
                newOrder.append(theList[3])  # 0,1,3
                newOrder.append(theList[2])  # 0,1,3,2
        elif m >= 5 and m <= 6:
            newOrder.append(theList[2])  # 0,2
            o = random.randint(1, 5)
            if o >= 1 and o <= 4:
                newOrder.append(theList[1])  # 0,2,1
                newOrder.append(theList[3])  # 0,2,1,3
            elif o == 5:
                newOrder.append(theList[3])  # 0,2,3
                newOrder.append(theList[1])  # 0,2,3,1
        elif m == 7:
            newOrder.append(theList[3])  # 0,3
            o = random.randint(1, 3)
            if o >= 1 and o <= 2:
                newOrder.append(theList[1])  # 0,3,1
                newOrder.append(theList[2])  # 0,3,1,2
            elif o == 3:
                newOrder.append(theList[2])  # 0,3,2
                newOrder.append(theList[1])  # 0,3,2,1

    elif n >= 9 and n <= 12:
        newOrder.append(theList[1])  # 1
        m = random.randint(1, 11)
        if m >= 1 and m <= 8:
            newOrder.append(theList[0])  # 1,0
            o = random.randint(1, 3)
            if o >= 1 and o <= 2:
                newOrder.append(theList[2])  # 1,0,2
                newOrder.append(theList[3])  # 1,0,2,3
            elif o == 3:
                newOrder.append(theList[3])  # 1,0,3
                newOrder.append(theList[2])  # 1,0,3,2
        elif m >= 9 and m <= 10:
            newOrder.append(theList[2])  # 1,2
            o = random.randint(1, 9)
            if o >= 1 and o <= 8:
                newOrder.append(theList[0])  # 1,2,0
                newOrder.append(theList[3])  # 1,2,0,3
            elif o == 9:
                newOrder.append(theList[3])  # 1,2,3
                newOrder.append(theList[0])  # 1,2,3,0
        elif m == 11:
            newOrder.append(theList[3])  # 1,3
            o = random.randint(1, 5)
            if o >= 1 and o <= 4:
                newOrder.append(theList[0])  # 1,3,0
                newOrder.append(theList[2])  # 1,3,0,2
            elif o == 5:
                newOrder.append(theList[2])  # 1,3,2
                newOrder.append(theList[0])  # 1,3,2,0

    elif n >= 13 and n <= 14:
        newOrder.append(theList[2])  # 2
        m = random.randint(1, 13)
        if m >= 1 and m <= 8:
            newOrder.append(theList[0])  # 2,0
            o = random.randint(1, 5)
            if o >= 1 and o <= 4:
                newOrder.append(theList[1])  # 2,0,1
                newOrder.append(theList[3])  # 2,0,1,3
            elif o == 5:
                newOrder.append(theList[3])  # 2,0,3
                newOrder.append(theList[1])  # 2,0,3,1
        elif m >= 9 and m <= 12:
            newOrder.append(theList[1])  # 2,1
            o = random.randint(1, 9)
            if o >= 1 and o <= 8:
                newOrder.append(theList[0])  # 2,1,0
                newOrder.append(theList[3])  # 2,1,0,3
            elif o == 9:
                newOrder.append(theList[3])  # 2,1,3
                newOrder.append(theList[0])  # 2,1,3,0
        elif m == 13:
            newOrder.append(theList[3])  # 2,3
            o = random.randint(1, 3)
            if o >= 1 and o <= 2:
                newOrder.append(theList[0])  # 2,3,0
                newOrder.append(theList[1])  # 2,3,0,1
            elif o == 3:
                newOrder.append(theList[1])  # 2,3,1
                newOrder.append(theList[0])  # 2,3,1,0

    elif n == 15:
        newOrder.append(theList[3])  # 3
        m = random.randint(1, 7)
        if m >= 1 and m <= 4:
            newOrder.append(theList[0])  # 3,0
            o = random.randint(1, 3)
            if o >= 1 and o <= 2:
                newOrder.append(theList[1])  # 3,0,1
                newOrder.append(theList[2])  # 3,0,1,2
            elif o == 3:
                newOrder.append(theList[2])  # 3,0,2
                newOrder.append(theList[1])  # 3,0,2,1
        elif m >= 5 and m <= 6:
            newOrder.append(theList[1])  # 3,1
            o = random.randint(1, 5)
            if o >= 1 and o <= 4:
                newOrder.append(theList[0])  # 3,1,0
                newOrder.append(theList[2])  # 3,1,0,2
            elif o == 5:
                newOrder.append(theList[2])  # 3,1,2
                newOrder.append(theList[0])  # 3,1,2,0
        elif m == 7:
            newOrder.append(theList[2])  # 3,2
            o = random.randint(1, 3)
            if o >= 1 and o <= 2:
                newOrder.append(theList[0])  # 3,2,0
                newOrder.append(theList[1])  # 3,2,0,1
            elif o == 3:
                newOrder.append(theList[1])  # 3,2,1
                newOrder.append(theList[0])  # 3,2,1,0

    return newOrder


# Testing code below

theList = [127, 60, 31, 204]
count = 0
count3 = 0

for x in range(64):
    res = randomWeightedSort(theList)
    print(res)
    if res[0] == 127:
        count += 1
    if res[0] == 204:
        count3 += 1

print(str(count)+' of roughly 34 expected')
print(str(count3)+' of roughly 4 expected')