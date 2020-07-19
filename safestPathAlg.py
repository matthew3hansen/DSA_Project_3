from Mapinit import mapFileName, streetNamesFileName, useNumbersInsteadOfStreetNames, Node, safeIntersectionWeight, \
    unsafeIntersectionWeight


# function that finds the number of rows and columns from the file
# and stores them in the passed in row and column variables
def findDimensionsOfMap():
    # open the csv file that contains the city map, in order to read in the data to create the map's nodes
    # second argument "r" is read-mode
    readFileObject = open(mapFileName, "r")

    # count number of rows in the file
    rowCount = 0
    for line in readFileObject:
        rowCount += 1

    # count number of columns in the file
    # reload the file since the previous row counting section moved the reading point to the end
    readFileObject = open(mapFileName, "r")
    # read in first line
    readInLine = readFileObject.readline()
    # remove the new line character at the end
    readInLine = readInLine.strip('\n')
    # make the string into a list, deliminated by commas
    readInLine = readInLine.split(',')
    # count up the number of elements in the list and that is the number of columns
    columnCount = len(readInLine)

    # close the previously opened csv file that contains the city map
    readFileObject.close()

    # return the row and column values
    return rowCount, columnCount


# read in from the file and create the map
# first, this function reads in street names for each latitude row and longitude column of the map,
# storing them in a "horizontalStreetNames" array as well as a "verticalStreetNames" array
# then this function creates a 2D array and populates it with created Nodes, if the associated map position isn't blocked
# then this 2-D map is scanned from left-to-right, up-to-down, tile by tile,
# during this scan, the Nodes are added to the newly created adjacency list, and the inner array for each added Node
# is populated with the unblocked nodes to the north, south, east, and west of that Node

def readFile(rows, columns):
    streetNamesFileObject = open(streetNamesFileName, "r")
    # arrays to store in the horizontal and vertical street names
    horizontalStreetNames = ["" for i in range(rows)]
    for i in range(0, rows):
        # read in single line
        readInLine = streetNamesFileObject.readline()
        # remove the new line character at the end
        readInLine = readInLine.strip('\n')
        # store into array
        horizontalStreetNames[i] = readInLine
    verticalStreetNames = ["" for j in range(columns)]
    for j in range(0, columns):
        # read in single line
        readInLine = streetNamesFileObject.readline()
        # remove the new line character at the end
        readInLine = readInLine.strip('\n')
        # store into array
        verticalStreetNames[j] = readInLine
    # close the previously opened street names file
    streetNamesFileObject.close()
    return verticalStreetNames, horizontalStreetNames


def insertNodes(rows, columns, verticalStreetNames, horizontalStreetNames):
    # open the csv file that contains the city map, in order to read in the data to create the map's nodes
    # second argument "r" is read-mode
    readFileObject = open(mapFileName, "r")
    # create array that will store the newly created Nodes
    # this array will be populated in a first 2-D for-loop
    # then the Nodes will be linked together in a second 2-D for-loop
    array = [[None for y in range(columns)] for x in range(rows)]
    # nested for-loop that reads in the map CSV file and populates the 2-D array of Nodes
    for i in range(0, rows):
        # read in single line
        readInLine = readFileObject.readline()
        # remove the new line character at the end
        readInLine = readInLine.strip('\n')
        # make the string into a list, deliminated by commas
        readInLine = readInLine.split(',')
        # nested inner for-loop
        j = 0
        for singleChar in readInLine:
            # if intersection is open
            if singleChar == 'O' or singleChar == 'L':
                array[i][j] = Node()
                # assign street name to intersection
                if useNumbersInsteadOfStreetNames == True:
                    array[i][j].intersectionName = str(i) + " / " + str(j)
                else:
                    array[i][j].intersectionName = horizontalStreetNames[i] + " / " + verticalStreetNames[j]
                # assign weight to intersection
                if singleChar == 'L':
                    array[i][j].weight = safeIntersectionWeight
                else:
                    array[i][j].weight = unsafeIntersectionWeight
            else:
                array[i][j] = None
            # iterate to next j index
            j += 1
    # close the previously opened .csv file that contains the city map
    readFileObject.close()
    return array


def createAdjacencyList(rows, columns):
    # open and read in street names
    verticalStreetNames, horizontalStreetNames = readFile(rows, columns)
    array = insertNodes(rows, columns, verticalStreetNames, horizontalStreetNames)

    """nested for-loop that populates an adjaency list
    this for-loop scans over the previously made 2-D map from left-to-right, up-to-down
    and adds not-blocked Nodes to the outer array, then an inner array data member of that Node is populated
    with the Nodes that are adjacent and not-blocked
    outer array storing the unique Nodes"""
    adjacencyList = []
    # dictionary that will map between a string intersection name with the relevant Node object
    intersectionNameDictionary = {}
    # counter variable to keep track of how many non-blocked Nodes are added to the adjacency list, for the above dictionary
    runningIndexOfList = -1
    for i in range(0, rows):
        for j in range(0, columns):
            # if the matrix element being iterated on is None (blocked intersection), then there
            # is no node, and no outgoing connections can be made, so just continueto the next element
            if array[i][j] == None:
                continue
            # otherwise, if the Node exists, create an entry to the dictionary that correlates the name
            # of the intersection with its index position in the adjacency array
            runningIndexOfList += 1
            intersectionNameDictionary[array[i][j].intersectionName] = runningIndexOfList
            adjacencyList.append(array[i][j])
            # check the four neighbors of the nodes, and add them to the inner array data member of the Node
            # add north if it exists
            if i - 1 >= 0 and array[i - 1][j] != None:
                adjacencyList[runningIndexOfList].adjacentNodes.append(array[i - 1][j])
            # add south if it exists
            if i + 1 < rows and array[i + 1][j] != None:
                adjacencyList[runningIndexOfList].adjacentNodes.append(array[i + 1][j])
            # add east if it exists
            if j + 1 < columns and array[i][j + 1] != None:
                adjacencyList[runningIndexOfList].adjacentNodes.append(array[i][j + 1])
            # add west if it exists
            if j - 1 >= 0 and array[i][j - 1] != None:
                adjacencyList[runningIndexOfList].adjacentNodes.append(array[i][j - 1])

    print("Loaded map from \"", mapFileName, "\" and street names from \"", streetNamesFileName, "\" successfully!",
          sep='')
    # return the created 2-D adjacency list
    return adjacencyList, intersectionNameDictionary


# take in a 2-D array adjacency list and its accompany dictionary
# and use Dijikstra's shortest path algorithm to find the shortest path to the destination
# only one path is found if there are multiple identical length paths
# finally, print out this path to the terminal
def findShortestPathAdjacencyList(adjacencyList, intersectionNameDictionary, sourceIntersectionName,
                                  destinationIntersectionName, usingNodesWeights):
    # first check if the input intersections exist at all in the adjacency list
    if (sourceIntersectionName not in intersectionNameDictionary.keys()):
        print("Specified source street intersection: \"", sourceIntersectionName,
              "\" was not recognized as a valid starting point.", sep='')
        return
    if (destinationIntersectionName not in intersectionNameDictionary.keys()):
        print("Specified destination street intersection: \"", destinationIntersectionName,
              "\" was not recognized as a valid starting point.", sep='')
        return

    # set the source intersection's "dist" value to 0
    adjacencyList[intersectionNameDictionary[sourceIntersectionName]].dist = 0
    # for-loop over all the unique nodes, performing Dijikstra's algorithm
    visitedCount = 0
    while (visitedCount != len(adjacencyList)):
        # first find the node with the lowest distance
        minDistance = float("inf")
        minIndex = 0
        for i in range(len(adjacencyList)):
            if (adjacencyList[i].visited == False and adjacencyList[i].dist < minDistance):
                minDistance = adjacencyList[i].dist
                minIndex = i
        # act upon the chosen minimum distance node
        # mark the chosen node as visited
        adjacencyList[minIndex].visited = True
        # set the distance of the chosen minimum distance node's neighbors
        for j in range(len(adjacencyList[minIndex].adjacentNodes)):
            if (usingNodesWeights == False):
                weight = 1
            else:
                weight = adjacencyList[minIndex].adjacentNodes[j].weight
            if (adjacencyList[minIndex].dist + weight < adjacencyList[minIndex].adjacentNodes[j].dist):
                adjacencyList[minIndex].adjacentNodes[j].dist = adjacencyList[minIndex].dist + weight
                # set this neighbor node's "previousPath" variable to record how it got to there
                if len(adjacencyList[minIndex].adjacentNodes[j].previousPath) == 0:
                    adjacencyList[minIndex].adjacentNodes[j].previousPath.append(adjacencyList[minIndex])
                else:
                    adjacencyList[minIndex].adjacentNodes[j].previousPath[0] = adjacencyList[minIndex]
        # iterate the counter and continue on the while loop
        visitedCount += 1
        # however, before continuing the loop, check if the just-visited node was the destination node,
        # and stop the while loop if it was
        if adjacencyList[minIndex].intersectionName == destinationIntersectionName:
            print("A single shortest path from: \"", sourceIntersectionName, "\" to \"", destinationIntersectionName,
                  "\" is:", sep='')
            if usingNodesWeights == True:
                print("(with taking account of crime map weights)")
            else:
                print("(with strictly by distance, ignoring crime map weights)")
            # create a stack and backtrack from the destination node, following each Node's "previousPath" variable
            pointerToPreviousNode = adjacencyList[minIndex]
            pathStack = []
            while (pointerToPreviousNode != None):
                pathStack.append(pointerToPreviousNode)
                if len(pointerToPreviousNode.previousPath) == 0:
                    break
                pointerToPreviousNode = pointerToPreviousNode.previousPath[0]
            print("Total number of steps to take: ", len(pathStack))
            # print out the route
            print("Start on: \"", pathStack[len(pathStack) - 1].intersectionName, "\"", sep='')
            pathStack.pop()
            stepCounter = 1
            while (len(pathStack) != 0):
                print("Step #", stepCounter, ": Go to street intersection \"",
                      pathStack[len(pathStack) - 1].intersectionName, "\"", sep='')
                pathStack.pop()
                stepCounter += 1
            print("\n\n")
            return
