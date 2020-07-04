#"defines (or C++ equivalent or whatever) here
mapFileName = "randomizedMapWithLights.csv"
streetNamesFileName = "streetNames.csv"


#Node class that will represent a street intersection
class Node: 
    #constructor with its instance variables
    def __init__(self, hasLighting):
        #strings to store the two street names of the intersection
        self.firstStreetName = ""
        self.secondStreetName = ""
        #bool variable that indicates if the street has lighting or not
        self.hasLighting = hasLighting
        #pointers to the four adjacent intersections, set to null by default
        self.west = None
        self.north = None
        self.east = None
        self.south = None
        #helper variables for later stuff like Dijkstra's shortest path algorithm
            #stores initial "infinite" value for Dijikstra calculations
        self.dist = float("inf")
            #weight variable for Dijikstra, in case we decide to add weights to street intersections later on or not
        self.weight = 1




#function that finds the number of rows and columns from the file
#and stores them in the passed in row and column variables
def findDimensionsOfMap():  
    #open the csv file that contains the city map, in order to read in the data to create the map's nodes
    #second argument "r" is read-mode
    readFileObject = open(mapFileName,"r")


    #count number of rows in the file
    rowCount = 0
    for line in readFileObject:
        rowCount += 1


    #count number of columns in the file
        #reload the file since the previous row counting section moved the reading point to the end
    readFileObject = open(mapFileName,"r")
        #read in first line
    readInLine = readFileObject.readline()
        #remove the new line character at the end
    readInLine = readInLine.strip('\n')
        #make the string into a list, deliminated by commas
    readInLine = readInLine.split(',')
        #count up the number of elements in the list and that is the number of columns
    columnCount = len(readInLine)


    #close the previously opened csv file that contains the city map
    readFileObject.close()

    #return the row and column values
    return rowCount, columnCount

#read in from the file and create the map
#first this function creates a 2D array and populates it with create Node's, if the associated map position isn't blocked
#then the nodes in the 2D array are linked to each other
def createMap(rows, columns):
    #open and read in street names
    streetNamesFileObject = open(streetNamesFileName, "r")
    #arrays to store in the horizontal and vertical street names
    horizontalStreetNames = ["" for i in range(rows)]
    for i in range(0, rows):
        #read in single line
        readInLine = streetNamesFileObject.readline()
        #remove the new line character at the end
        readInLine = readInLine.strip('\n')
        #store into array
        horizontalStreetNames[i] = readInLine
    verticalStreetNames = ["" for j in range(columns)]
    for j in range(0, columns):
        #read in single line
        readInLine = streetNamesFileObject.readline()
        #remove the new line character at the end
        readInLine = readInLine.strip('\n')
        #store into array
        verticalStreetNames[j] = readInLine
    #close the previously opened street names file
    streetNamesFileObject.close()
    
    
    #open the csv file that contains the city map, in order to read in the data to create the map's nodes
    #second argument "r" is read-mode
    readFileObject = open(mapFileName,"r")

    #create array that will store the newly created Node's
    #this array will be populated in a first 2-D for-loop
    #then the Nodes will be linked together in a second 2-D for-loop
    array = [[None for y in range(columns)] for x in range(rows)] 


    #first 2-D for-loop that populates the array of Nodes
        #store the index values of the first Node created, so that this initial Node can be returned to represent the graph
        #this will probably be, [0,0]
    initialNodeI = -1
    initialNodeJ = -1
    firstNodeFound = False
    for i in range(0, rows):
        #read in single line
        readInLine = readFileObject.readline()
        #remove the new line character at the end
        readInLine = readInLine.strip('\n')
        #make the string into a list, deliminated by commas
        readInLine = readInLine.split(',')
       
            #create j index for inner loop
        j = 0
        for singleChar in readInLine:
            #if intersection is open
            if singleChar == 'O' or singleChar == 'L':
                #store index values of first created node (which will probably be [0, 0] but could vary depending on the city map input)
                if(firstNodeFound == False):
                    initialNodeI = i
                    initialNodeJ = j
                    firstNodeFound = True

                #if intersection is not lit ('O')
                if singleChar == 'O':
                    array[i][j] = Node(False)
                #if intersection is lit ('L')
                else:
                    array[i][j] = Node(True)

                #assign street name to intersection
                array[i][j].firstStreetName = horizontalStreetNames[i]
                array[i][j].secondStreetName = verticalStreetNames[j]
            else:
                array[i][j] = None
            #iterate to next j index
            j += 1
    #close the previously opened .csv file that contains the city map
    readFileObject.close()



    #second 2-D for-loop that links the nodes together
    #the for-loop will, on each element it visits, create outgoing links to the adjacent nodes if they are
    #not out of bounds and if they are not a blocked intersection (which in the created 2D array is a "None" value)
        #i outer-loop
    for i in range(0, rows):
        #j inner-loop
        for j in range(0, columns):
            #if the matrix element being iterated on is None (blocked intersection), then there
            #is no node, and no outgoing connections can be made, so just continueto the next element
            if array[i][j] == None:
                continue

            #Otherwise, if the Node exists, make the cardinal outgoing connections
            #link north
            if i - 1 >= 0 and array[i-1][j] != None:
                array[i][j].north = array[i-1][j]
            #link south
            if i + 1 < rows and array[i+1][j] != None:
                array[i][j].south = array[i+1][j]
            #link east
            if j + 1 < columns and array[i][j + 1] != None:
                array[i][j].east = array[i][j + 1]
            #link west
            if j - 1 >= 0 and array[i][j - 1] != None:
                array[i][j].west = array[i][j - 1]

    print("Loaded map from \"", mapFileName, "\" and street names from \"", streetNamesFileName,"\" successfully!", sep = '')
    #return the first node (top-most and left-mode node which is probably [0, 0]
    #this first node has connections to all the other created nodes, so it's the graph
    return array[initialNodeI][initialNodeJ]

#traverse the map for debugging purposes
def exploreGraph(createdGraph):
    currentNode = createdGraph
    print()
    print("You started on road intersection:", currentNode.firstStreetName, " / ", currentNode.secondStreetName)
    userInput = input("Enter in direction to move (\"n\", \"s\", \"e\", \"w\") or \"exit\" to exit: ")

    while(userInput != "exit"):
        #if the command was one of the cardinal directions, see if you can move there
        #and if you can, then move there
        #if you can't then stay where you were
        if(userInput == "n"):
            if(currentNode.north == None):
                print("Can not move North, either it is blocked or off the map.")
                print("You remain on road intersection:", currentNode.firstStreetName, " / ", currentNode.secondStreetName)
            else:
                currentNode = currentNode.north
                print("You moved North to road intersection:", currentNode.firstStreetName, " / ", currentNode.secondStreetName)
        elif(userInput == "s"):
            if(currentNode.south == None):
                print("Can not move South, either it is blocked or off the map.")
                print("You remain on road intersection:", currentNode.firstStreetName, " / ", currentNode.secondStreetName)
            else:
                currentNode = currentNode.south
                print("You moved South to road intersection:", currentNode.firstStreetName, " / ", currentNode.secondStreetName)
        elif(userInput == "e"):
            if(currentNode.east == None):
                print("Can not move East, either it is blocked or off the map.")
                print("You remain on road intersection:", currentNode.firstStreetName, " / ", currentNode.secondStreetName)
            else:
                currentNode = currentNode.east
                print("You moved East to road intersection:", currentNode.firstStreetName, " / ", currentNode.secondStreetName)
        elif(userInput == "w"):
            if(currentNode.west == None):
                print("Can not move West, either it is blocked or off the map.")
                print("You remain on road intersection:", currentNode.firstStreetName, " / ", currentNode.secondStreetName)
            else:
                currentNode = currentNode.west
                print("You moved West to road intersection:", currentNode.firstStreetName, " / ", currentNode.secondStreetName)

        #prompt for more commands
        print()
        userInput = input("Enter in direction to move (\"n\", \"s\", \"e\", \"w\") or \"exit\" to exit: ")

    print("Graph Exploration done ----- exiting!")


#MAIN FUNCTION
if __name__ == '__main__':
    #first find the dimensions of the map
    rows, columns = findDimensionsOfMap()

    #call function to create map and store the single returned node from which the rest of the graph can be accessed
    createdGraph = createMap(rows, columns)

    #debugging explore graph function to see if graph was linked correctly between its nodes
    exploreGraph(createdGraph)