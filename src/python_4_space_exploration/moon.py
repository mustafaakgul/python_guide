# Count the number of Moon rocks by type using Python

print("Artemis Rover Rock Scanner Starting")
basalt = 0
breccia = 0
highland = 0
regolith = 0
rockList = []

strPath = "rocks.txt"

fileObject = open(strPath, "w")
fileObject.writelines(["Reading Rocks\n","basalt\n","breccia\n","highland\n","regolith\n","highland\n","breccia\n","highland\n","regolith\n","regolith\n","basalt\n","highland\n","basalt\n","breccia\n","breccia\n","regolith\n","breccia\n","highland\n","highland\n","breccia\n","basalt\n"])
fileObject.close()

fileObject = open(strPath)
line = fileObject.readline()
print(line)

rockList = fileObject.readlines()
for rock in rockList:
    print(rock)
fileObject.close()


def countMoonRocks(rockToID):
    global basalt
    global breccia
    global highland
    global regolith

    rockToID = rockToID.lower()

    if("basalt" in rockToID):
        print("Found a basalt\n")
        basalt += 1
    elif("breccia" in rockToID):
        print("Found a breccia\n")
        breccia += 1
    elif("highland" in rockToID):
        print("Found a highland\n")
        highland += 1
    elif("regolith" in rockToID):
        print("Found a regolith\n")
        regolith += 1

    return