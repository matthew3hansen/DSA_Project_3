import csv
import random
import time


def floodfill(storeArray,i,j):
    GRIDSIZE = 500
    if storeArray[i][j] == '0' or storeArray[i][j] == 'A':
        return
    else:
        storeArray[i][j] = 'A'

    xStack = []
    yStack = []

    if i-1 >= 0:
        xStack.append(i-1)
        yStack.append(j)
    if i+1 < GRIDSIZE:
        xStack.append(i + 1)
        yStack.append(j)
    if j-1 >= 0:
        xStack.append(i)
        yStack.append(j-1)
    if j+1 < GRIDSIZE:
        xStack.append(i)
        yStack.append(j+1)

    while xStack:
        if storeArray[xStack[0]][yStack[0]] == 'A' or storeArray[xStack[0]][yStack[0]] == '0':
            xStack.pop()
            yStack.pop()
        else:
            storeArray[xStack[0]][yStack[0]] = 'A'

        if xStack[0]-1 >= 0:
            xStack.append(xStack[0] - 1)
            yStack.append(yStack[0])
        if xStack[0]+1 < GRIDSIZE:
            xStack.append(xStack[0]+1)
            yStack.append(yStack[0])
        if yStack[0]-1 >= 0:
            xStack.append(xStack[0])
            yStack.append(yStack[0]-1)
        if yStack[0] + 1 < GRIDSIZE:
            xStack.append(xStack[0])
            yStack.append(yStack[0]+1)

        xStack.pop()
        yStack.pop()








def checkIfNotEnclosed(storeArray,i,j):
    floodfill(storeArray,i,j)

    if storeArray[0][0] == 'A':
        return True
    else:
        return False


if __name__ == '__main__':
    GRIDSIZE = 500
    PERCENTBUILDINGS = 20
    RANGEOFCRIMEVALUES = 9
    random.seed(time.time())

    storeArray = [[0 for x in range(GRIDSIZE)] for y in range(GRIDSIZE*2)]
    

    for i in range(0,GRIDSIZE):
        for j in range(0, GRIDSIZE):
            randomNumber = random.random() % 100 + 1
            if randomNumber <= PERCENTBUILDINGS:
                storeArray[i][j] = '0'
            else:
                randomInt = random.random() % RANGEOFCRIMEVALUES + 1
                storeArray[i][j] = str(randomInt) + '0'
    # Make borders clear

    for i in range(0, GRIDSIZE):
        randomInt = random.random() % RANGEOFCRIMEVALUES + 1
        storeArray[0][i] = str(randomInt) + '0'
        randomInt = random.random() % RANGEOFCRIMEVALUES + 1
        storeArray[GRIDSIZE-1][i] = str(randomInt) + '0'
        randomInt = random.random() % RANGEOFCRIMEVALUES + 1
        storeArray[i][GRIDSIZE-1] = str(randomInt) + '0'

    temp = [[0 for x in range(GRIDSIZE)] for y in range(GRIDSIZE)]
    for i in range(0,GRIDSIZE-1):
        for j in range(0,GRIDSIZE-1):
            if temp[i][j] == '0' or temp[i][j] == 'A':
                continue

            # reset temp array
            for i in range(0, GRIDSIZE):
                for j in range(0, GRIDSIZE):
                    temp[i][j] = storeArray[i][j]
            shiftCount = 1
            while checkIfNotEnclosed(temp,i,j)!= True:
                print("Found index ",i, " ", j, "that is completely enclosed, blindly opening up one block to the left and checking again.\n ")
                randomInt = random.random() % RANGEOFCRIMEVALUES + 1
                storeArray[i-shiftCount][j] = str(randomInt) + '0'
                shiftCount += 1

                for i in range(0,GRIDSIZE):
                    for j in range(0,GRIDSIZE):
                        temp[i][j] = storeArray[i][j]
    for i in range(0,GRIDSIZE):
        j = GRIDSIZE-1
        while j != -1:
            storeArray[i][2*j] = storeArray[i][j]
            storeArray[i][2*j+1] = ','
            j -= 1

    with open('newRandomMap.csv', mode='w') as newRandomMap:
        for i in range(0,GRIDSIZE):
            for j in range(0,GRIDSIZE*2-1):
                newRandomMap = storeArray[i][j]
            newRandomMap = "\n"




