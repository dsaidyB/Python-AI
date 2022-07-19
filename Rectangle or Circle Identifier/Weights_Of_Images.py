activationNumber = 1

def getWeightValues(file):
    weightValues = []
    f = open(file, "r")
    for i in f:
        row = []
        j = 0
        currentVal = ""
        while j < len(i):
            if (i[j] == ","):
                row.append(currentVal)
                j += 1
                currentVal = ""
            elif (i[j] == "\n"):
                j += 1
            else:
                currentVal += i[j]
                j += 1
        weightValues.append(row)
    f.close()
    # print(weightValues)
    return weightValues

def trainModel(trainingFile):
    trainingModel = getWeightValues("Pixel Value Weights.txt")
    # print(trainingModel) idk why index 99 no work on this

    trainingObject = getWeightValues(trainingFile)
    # print(trainingObject[98][98])

    answer = trainingFile[:6]
    # print(answer)
    print("File is: " + trainingFile)

    total = 0

    for a in range(0, 99):
        for b in range(0, 99):
            total += int(trainingModel[a][b]) * int(trainingObject[a][b])

    if (total > activationNumber):
        print("Guess is: Circle")
        if (answer != "Circle"):
            for x in range(0, 100):
                for y in range(0, 100):
                    if trainingObject[x][y] == "1":
                        trainingModel[x][y] = str(int(trainingModel[x][y]) - 1)
    else:
        print("Guess is: Rectangle")
        if (answer == "Circle"):
            for x in range(0, 100):
                for y in range(0, 100):
                    if trainingObject[x][y] == "1":
                        trainingModel[x][y] = str(int(trainingModel[x][y]) + 1)

    # print(trainingModel)

    f = open("Pixel Value Weights.txt", "w")
    f.write("")
    f.close()

    f = open("Pixel Value Weights.txt", "a")
    for r in range(0, len(trainingModel) - 1):
        f.write(",".join(trainingModel[r]) + ",\n")
    f.write(",".join(trainingModel[-1])+",")
    f.close()

    print("Model Updated")
    print()

# for n in range(1,11):
#     trainModel("Rectangles/Training Rectangles/Training Rectangle " + str(n) + " Values.txt")
#     trainModel("Circles/Training Circles/Training Circle " + str(n) + " Values.txt")

def applyModel(checkFile):
    trainingModel = getWeightValues("Pixel Value Weights.txt")
    trainingObject = getWeightValues(checkFile)
    print("File is: " + checkFile)

    total = 0
    for a in range(0, 99):
        for b in range(0, 99):
            total += int(trainingModel[a][b]) * int(trainingObject[a][b])

    if (total > activationNumber):
        print("Guess is: Circle")
    else:
        print("Guess is: Rectangle")

    print()


applyModel("Circles/Training Circles/Training Circle 1 Values.txt")
applyModel("Circles/Test Circles/Test Circle 1 Values.txt")
applyModel("Rectangles/Test Rectangles/Test Rectangle 1 Values.txt")
applyModel("Circles/Test Circles/Test Circle 2 Values.txt")
applyModel("Rectangles/Training Rectangles/Training Rectangle 7 Values.txt")
