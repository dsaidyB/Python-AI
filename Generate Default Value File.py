imagePixels = []

for i in range(0, 100):
    row = ""
    for j in range(0, 100):
        row += "0,"
    imagePixels.append(row)

f = open("Pixel Value Weights.txt", "w")
f.write("")
f.close()

f = open("Pixel Value Weights.txt", "a")
for x in range(0, 99):
    f.write(imagePixels[x] + "\n")
f.write(imagePixels[99])
f.close()
