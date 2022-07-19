from PIL import Image

def getPixelData(folder, trainingSize):
    for n in range(1, trainingSize+1):
        im = Image.open(folder + " " + str(n) + ".jpg")

        # px = list(im.getdata())
        # print(px)
        # for x in px:
        #     if x[0] < 200 and x[1] < 200 and x[2] < 200:
        #         print("1")
        #     else:
        #         print("0")

        imagePixels = []

        for i in range(0, 100):
            row = ""
            for j in range(0, 100):
                pixVal = im.getpixel((j, i))
                if pixVal[0] < 200 and pixVal[1] < 200 and pixVal[2] < 200:
                    row += "1,"
                else:
                    row += "0,"
            imagePixels.append(row)

        # for x in imagePixels:
        #     print(x)
        # print(imagePixels)

        f = open(folder + " " + str(n) + " Values.txt", "w")
        f.write("")
        f.close()

        f = open(folder + " " + str(n) + " Values.txt", "a")
        for x in range(0,99):
            f.write(imagePixels[x]+"\n")
        f.write(imagePixels[99])
        f.close()

        # if wrong subtract
        # if correct add

getPixelData("Circles/Training Circles/Training Circle", 10)
getPixelData("Rectangles/Training Rectangles/Training Rectangle", 10)
getPixelData("Circles/Test Circles/Test Circle", 2)
getPixelData("Rectangles/Test Rectangles/Test Rectangle", 2)
