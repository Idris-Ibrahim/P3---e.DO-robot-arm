def DefineBoxes():

    #defining the list of boxes and the objekt for a box
    BoxList = []

    class Box:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
            self.volume = self.x * self.y * self.z

    #Amount of box types:
    BoxAmount = int(input("Amount of box types: "))

    #insert measurement for each axes for each box:
    i = 0
    while BoxAmount > 0 :
        x = float(input(f"Box {i} x length: "))
        y = float(input(f"Box {i} y length: "))
        z = float(input(f"Box {i} z length: "))

        BoxList.append(Box(x, y, z))

        i += 1
        BoxAmount -= 1
        print("\n")
    
    #print all the boxes and the measurement:
    for i in range (0,len(BoxList)):

        print(f"Box {i}:", BoxList[i].x, BoxList[i].y, BoxList[i].z)
        print(f"Box {i} volume: {BoxList[i].volume}")

#Run function:
DefineBoxes()