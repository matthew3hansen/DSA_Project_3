#imports here
import time

#toggle-able variables here (e.g. "define" variables)
mapFileName = "small_grid.csv"
streetNamesFileName = "streetNames.csv"
useNumbersInsteadOfStreetNames = True


#Node class that will represent a street intersection
class Node: 
    #constructor with its instance variables
    def __init__(self):
        #string to store the street intersection name (which should be in format example: "Baker / Wilson")
        self.intersectionName = "";
        #inner array for use in an adjacency array
        self.adjacentNodes = []
        #distance value for Dijikstra calculations
        self.dist = float("inf")
        #weight of the Node, for Dijikstra
        self.weight = float("inf")
        #storing the path(s) used for Dijikstra
        self.previousPath = []

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
#first, this function reads in street names for each latitude row and longitude column of the map,
#storing them in a "horizontalStreetNames" array as well as a "verticalStreetNames" array
#then this function creates a 2D array and populates it with created Nodes, if the associated map position isn't blocked
#then this 2-D map is scanned from left-to-right, up-to-down, tile by tile,
#during this scan, the Nodes are added to the newly created adjacency list, and the inner array for each added Node
#is populated with the unblocked nodes to the north, south, east, and west of that Node
def createArray(rows, columns):
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
    #create array that will store the newly created Nodes
    #this array will be populated in a first 2-D for-loop
    #then the Nodes will be linked together in a second 2-D for-loop
    array = [[None for y in range(columns)] for x in range(rows)]
    #nested for-loop that reads in the map CSV file and populates the 2-D array of Nodes
    for i in range(0, rows):
        #read in single line
        readInLine = readFileObject.readline()
        #remove the new line character at the end
        readInLine = readInLine.strip('\n')
        #make the string into a list, deliminated by commas
        readInLine = readInLine.split(',')
        #nested inner for-loop
        j = 0
        for singleChar in readInLine:
            #if intersection is open
            if singleChar != '0' and singleChar != '':
                array[i][j] = Node()
                #assign street name to intersection
                if useNumbersInsteadOfStreetNames == True:
                    array[i][j].intersectionName = str(i) + " / " + str(j)
                else:
                    array[i][j].intersectionName = horizontalStreetNames[i] + " / " + verticalStreetNames[j]
                #assign weight to intersection
                array[i][j].weight = int(singleChar)
            elif singleChar != '':
                array[i][j] = None
            #iterate to next j index
            j += 1
    #close the previously opened .csv file that contains the city map
    readFileObject.close()
    return array


def createAdjacencyList(array, rows, columns):
    #keep track of the execution time to output at the end of the function
    startTime = time.time()
    #nested for-loop that populates an adjaency list
    #this for-loop scans over the previously made 2-D map from left-to-right, up-to-down
    #and adds not-blocked Nodes to the outer array, then an inner array data member of that Node is populated
    #with the Nodes that are adjacent and not-blocked
        #outer array storing the unique Nodes
    adjacencyList = []
    #dictionary that will map between a string intersection name with the relevant Node object
    intersectionNameDictionary = {}
    #counter variable to keep track of how many non-blocked Nodes are added to the adjacency list, for the above dictionary
    runningIndexOfList = -1
    for i in range(0, rows):
        for j in range(0, columns):
            #if the matrix element being iterated on is None (blocked intersection), then there
            #is no node, and no outgoing connections can be made, so just continueto the next element
            if array[i][j] == None:
                continue
            #otherwise, if the Node exists, create an entry to the dictionary that correlates the name
            #of the intersection with its index position in the adjacency array
            runningIndexOfList += 1
            intersectionNameDictionary[array[i][j].intersectionName] = runningIndexOfList
            adjacencyList.append(array[i][j])
            #check the four neighbors of the nodes, and add them to the inner array data member of the Node
            #add north if it exists
            if i - 1 >= 0 and array[i-1][j] != None:
                adjacencyList[runningIndexOfList].adjacentNodes.append((array[i-1][j], "N"))
            #add south if it exists
            if i + 1 < rows and array[i+1][j] != None:
                adjacencyList[runningIndexOfList].adjacentNodes.append((array[i+1][j], "S"))
            #add east if it exists
            if j + 1 < columns and array[i][j + 1] != None:
                adjacencyList[runningIndexOfList].adjacentNodes.append((array[i][j + 1], "E"))
            #add west if it exists
            if j - 1 >= 0 and array[i][j - 1] != None:
                adjacencyList[runningIndexOfList].adjacentNodes.append((array[i][j - 1], "W"))

    print("Loaded map from \"", mapFileName, "\" and street names from \"", streetNamesFileName,"\" successfully! ", sep = '')
    print("Map loading execution time was:", (time.time() - startTime), "seconds")
    print()
    #return the created 2-D adjacency list
    return adjacencyList, intersectionNameDictionary

#take in a 2-D array adjacency list and its accompany dictionary
#and use Dijikstra's shortest path algorithm to find the shortest path to the destination
#only one path is found if there are multiple identical length paths
#finally, print out this path to the terminal
def findShortestPathSingle(adjacencyList, intersectionNameDictionary, sourceIntersectionName, destinationIntersectionName, usingNodesWeights):
    #keep track of the execution time to output at the end of the function
    startTime = time.time()
    #first check if the input intersections exist at all in the adjacency list
    if(sourceIntersectionName not in intersectionNameDictionary.keys()):
        print("Specified source street intersection: \"", sourceIntersectionName, "\" was not recognized as a valid starting point.\n", sep = '')
        return
    if(destinationIntersectionName not in intersectionNameDictionary.keys()):
        print("Specified destination street intersection: \"", destinationIntersectionName, "\" was not recognized as a valid starting point.\n", sep = '')
        return
    #check if the source and destination are the same
    if(sourceIntersectionName == destinationIntersectionName):
        print("Specified source and destination street intersections: \"", destinationIntersectionName, "\" are the same, please enter different points.\n", sep = '')
        return

    #set the source intersection's "dist" value to 0
    adjacencyList[intersectionNameDictionary[sourceIntersectionName]].dist = 0
    #for-loop over all the unique nodes, performing Dijikstra's algorithm
    while(len(adjacencyList) != 0):
        #first find the node with the lowest distance
        minDistance = float("inf")
        minIndex = 0
        for i in range(len(adjacencyList)):
            if (adjacencyList[i].dist < minDistance):
                minDistance = adjacencyList[i].dist
                minIndex = i
        #act upon the chosen minimum distance node
        #set the distance of the chosen minimum distance node's neighbors
        for j in range(len(adjacencyList[minIndex].adjacentNodes)):
            if(usingNodesWeights == False):
                weight = 1
            else:
                weight = adjacencyList[minIndex].adjacentNodes[j][0].weight
            if (adjacencyList[minIndex].dist + weight < adjacencyList[minIndex].adjacentNodes[j][0].dist):
                adjacencyList[minIndex].adjacentNodes[j][0].dist = adjacencyList[minIndex].dist + weight
                #set this neighbor node's "previousPath" variable to record how it got to there
                if len(adjacencyList[minIndex].adjacentNodes[j][0].previousPath) == 0:
                    adjacencyList[minIndex].adjacentNodes[j][0].previousPath.append(adjacencyList[minIndex])
                else:
                    adjacencyList[minIndex].adjacentNodes[j][0].previousPath[0] = adjacencyList[minIndex]
        #before continuing the loop, check if the just-visited node was the destination node,
        #and stop the while loop if it was
        if adjacencyList[minIndex].intersectionName == destinationIntersectionName:
            print("A single shortest path from: \"", sourceIntersectionName, "\" to \"", destinationIntersectionName, "\" is:", sep='')
            if usingNodesWeights == True:
                print("(with taking account of crime map weights)")
            else:
                print("(with strictly by distance, ignoring crime map weights)")
            #create a stack and backtrack from the destination node, following each Node's "previousPath" variable
            pointerToPreviousNode = adjacencyList[minIndex]
            pathStack = []
            while(pointerToPreviousNode != None):
                pathStack.append(pointerToPreviousNode)
                if len(pointerToPreviousNode.previousPath) == 0:
                    break
                pointerToPreviousNode = pointerToPreviousNode.previousPath[0]
            print("Total number of steps to take:", len(pathStack) - 1)
            #print out the route
            print("Start on: \"", pathStack[len(pathStack) - 1].intersectionName, "\"", sep='')
            pathStack.pop()
            stepCounter = 1
            while(len(pathStack) != 0):
                print("Step #", stepCounter, ": Go to street intersection \"", pathStack[len(pathStack) - 1].intersectionName, "\"", sep='')
                pathStack.pop()
                stepCounter += 1
            print("Diijkstra's shortest path algorithm for a single path execution time was :", (time.time() - startTime), "seconds")
            print()
            return
        #before continuing on the while loop,
        #remove the visited Node from the adjacency list so that it is no longer scanned in future runs of the while loop
        adjacencyList.pop(minIndex)

#do the same as the "findShortestPathSingle()" function above,
#except find multiple paths if there are multiple routes of the same shortest-length
def findShortestPathMultiple(adjacencyList, intersectionNameDictionary, sourceIntersectionName, destinationIntersectionName, usingNodesWeights):
    #keep track of the execution time to output at the end of the function
    startTime = time.time()
    #first check if the input intersections exist at all in the adjacency list
    if(sourceIntersectionName not in intersectionNameDictionary.keys()):
        print("Specified source street intersection: \"", sourceIntersectionName, "\" was not recognized as a valid starting point.\n", sep = '')
        return
    if(destinationIntersectionName not in intersectionNameDictionary.keys()):
        print("Specified destination street intersection: \"", destinationIntersectionName, "\" was not recognized as a valid starting point.\n", sep = '')
        return
    #check if the source and destination are the same
    if(sourceIntersectionName == destinationIntersectionName):
        print("Specified source and destination street intersections: \"", destinationIntersectionName, "\" are the same, please enter different points.\n", sep = '')
        return

    #set the source intersection's "dist" value to 0
    adjacencyList[intersectionNameDictionary[sourceIntersectionName]].dist = 0
    #used to know when to stop calculating paths
    destinationNodeMinimumDistance = float("inf")
    destinationNodeIndex = -1
    while(len(adjacencyList) != 0):
        #first find the node with the lowest distance
        minDistance = float("inf")
        minIndex = 0
        for i in range(len(adjacencyList)):
            if (adjacencyList[i].dist < minDistance):
                minDistance = adjacencyList[i].dist
                minIndex = i
        #act upon the chosen minimum distance node
        #set the distance of the chosen minimum distance node's neighbors
        for j in range(len(adjacencyList[minIndex].adjacentNodes)):
            if(usingNodesWeights == False):
                weight = 1
            else:
                weight = adjacencyList[minIndex].adjacentNodes[j][0].weight
            if (adjacencyList[minIndex].dist + weight < adjacencyList[minIndex].adjacentNodes[j][0].dist):
                adjacencyList[minIndex].adjacentNodes[j][0].dist = adjacencyList[minIndex].dist + weight
                #set this neighbor node's "previousPath" variable to record how it got to there
                adjacencyList[minIndex].adjacentNodes[j][0].previousPath.clear()
                adjacencyList[minIndex].adjacentNodes[j][0].previousPath.append(adjacencyList[minIndex])
            elif (adjacencyList[minIndex].dist + weight == adjacencyList[minIndex].adjacentNodes[j][0].dist):
                #add this alternate path to the "previousPath" variable
                adjacencyList[minIndex].adjacentNodes[j][0].previousPath.append(adjacencyList[minIndex])
        #however, before continuing the loop, check if the just-visited node was the destination node, in which case,
        #store the minimum distance and index of that destination node
        if adjacencyList[minIndex].intersectionName == destinationIntersectionName:
            destinationNodeMinimumDistance = adjacencyList[minIndex].dist
            destinationNodeIndex = minIndex
        #if the currently iterated on Node has a dist higher than the destination node's, then all paths to the destination node have
        #already been found, so end the algorithm's while loop
        if adjacencyList[minIndex].dist > destinationNodeMinimumDistance:
            print("A single shortest path from: \"", sourceIntersectionName, "\" to \"", destinationIntersectionName, "\" is:", sep='')
            if usingNodesWeights == True:
                print("(with taking account of crime map weights)")
            else:
                print("(with strictly by distance, ignoring crime map weights)")
            #create a 2-D array representing the multiple paths possible
            #and backtrack from the destination node, following each Node's "previousPath" possible variable
            #creating a new inner array for each branching path
            pathStack = []
            pathStack.append([])
            pathStack[0].append(adjacencyList[destinationNodeIndex])
            jIndex = -1
            sourceReached = False
            while(sourceReached == False):
                jIndex += 1
                originalArrayLength = len(pathStack)
                index = 0
                for i in range(originalArrayLength):
                    #if there are multiple entries in the looked at Node's previous path array,
                    #then insert new subarrays and copy the path from the "parent" subarray,
                    #to represent branching of paths
                    #and then extend each of these subarrays with the different Nodes in the path array
                    if(len(pathStack[index][jIndex].previousPath) > 1):
                        for j in range(len(pathStack[index][jIndex].previousPath) - 1):
                            newSubarray = list(pathStack[index])
                            pathStack.insert(index + 1, newSubarray)
                        for j in range(len(pathStack[index][jIndex].previousPath)):
                            pathStack[index + j].append(pathStack[index][jIndex].previousPath[j])
                        index += len(pathStack[index][jIndex].previousPath)
                    #otherwise, if there is just one entry in the looked at Node's previous path,
                    #then don't add any new subarrays, and just extend the subarray with the next node
                    else:
                        pathStack[index].append(pathStack[index][jIndex].previousPath[0])
                        index += 1
                if pathStack[0][jIndex].previousPath[0].intersectionName == sourceIntersectionName:
                    sourceReached = True
            print("Total number of steps to take:", len(pathStack[0]) - 1)
            print(len(pathStack), "equivalent minimum length paths were found.")
            print()
            #print out the routes
            for i in range(len(pathStack)):
                print("POSSIBLE PATH #", i + 1, sep='')
                print("Start on: \"", pathStack[i][len(pathStack[i]) - 1].intersectionName, "\"", sep='')
                pathStack[i].pop()
                stepCounter = 1
                while(len(pathStack[i]) != 0):
                    print("Step #", stepCounter, ": Go to street intersection \"", pathStack[i][len(pathStack[i]) - 1].intersectionName, "\"", sep='')
                    pathStack[i].pop()
                    stepCounter += 1
                print()
            print("Diijkstra's shortest path algorithm for multiple paths execution time was :", (time.time() - startTime), "seconds")
            return
        #before continuing on the while loop,
        #remove the visited Node from the adjacency list so that it is no longer scanned in future runs of the while loop
        adjacencyList.pop(minIndex)

def shortest_path_visual(aList, source):
    #keep track of the execution time to output at the end of the function
    start_time = time.time()

    #Dictionaries to keep tract of total weights, and previous nodes, and computed
    weight_map = {}
    previous_map = {}
    computed = []

    for element in aList:
        if element.intersectionName != aList[source].intersectionName:
            weight_map[element.intersectionName] = 900000
            previous_map[element.intersectionName] = -1
        else:
            weight_map[element.intersectionName] = 0
            previous_map[element.intersectionName] = -1

    while(len(computed) != len(aList)):
        min_index = 0
        counter = 0
        min_value = 999999999
        for name, value in weight_map.items():
            if value < min_value:
                if computed.count(aList[counter]) == 0:
                    min_value = value
                    min_index = counter
            counter += 1

        computed.append(aList[min_index])
        for i in range(len(aList[min_index].adjacentNodes)):
            if min_value + aList[min_index].adjacentNodes[i][0].weight < weight_map[aList[min_index].adjacentNodes[i][0].intersectionName]:
                weight_map[aList[min_index].adjacentNodes[i][0].intersectionName] = min_value + aList[min_index].adjacentNodes[i][0].weight
                previous_map[aList[min_index].adjacentNodes[i][0].intersectionName] = aList[min_index].intersectionName

    return weight_map, previous_map

#MAIN FUNCTION
if __name__ == '__main__':
    #first find the dimensions of the map
    rows, columns = findDimensionsOfMap()
    array = createArray(rows, columns)
    adjacencyList, intersectionNameDictionary = createAdjacencyList(array, rows, columns)
    #COMMAND MENU
    '''
    userInput = input("Enter \"1\" to find a single shortest path, enter \"2\" to find multiple shortest paths, enter \"exit\" to exit: ")
    while(userInput != "exit"):
        #if the command was one of the cardinal directions, see if you can move there
        #and if you can, then move there
        #if you can't then stay where you were
        if(userInput == "1"):
            sourceIntersectionName = input("Enter name of starting street intersection (e.g. \"Baker / Wilson\"): ")
            destinationIntersectionName = input("Enter name of destination street intersection (e.g. \"Chevrolet / Sushi\"): ")
            weightMode = input("Factor in crime map? (\"y\") or find the strictly shortest physical path (\"n\")?: ")
            while(weightMode != "y" and weightMode != "n"):
                weightMode = input("Factor in crime map? (\"y\") or find the strictly shortest physical path (\"n\")?: ")
            #load the map
            adjacencyList, intersectionNameDictionary = createAdjacencyList(array, rows, columns)
            if(weightMode == "y"):
                #execute Diikstra's algorithm for single path
                findShortestPathSingle(adjacencyList, intersectionNameDictionary, sourceIntersectionName, destinationIntersectionName, True)
            else:
                #execute Diikstra's algorithm for single path
                findShortestPathSingle(adjacencyList, intersectionNameDictionary, sourceIntersectionName, destinationIntersectionName, False)
        elif(userInput == "2"):
            sourceIntersectionName = input("Enter name of starting street intersection (e.g. \"Baker / Wilson\"): ")
            destinationIntersectionName = input("Enter name of destination street intersection (e.g. \"Chevrolet / Sushi\"): ")
            weightMode = input("Factor in crime map? (\"y\") or find the strictly shortest physical path (\"n\")?: ")
            while(weightMode != "y" and weightMode != "n"):
                weightMode = input("Factor in crime map? (\"y\") or find the st1ictly shortest physical path (\"n\")?: ")
            #load the map
            adjacencyList, intersectionNameDictionary = createAdjacencyList(array, rows, columns)
            if(weightMode == "y"):
                #execute Diikstra's algorithm for single path
                findShortestPathMultiple(adjacencyList, intersectionNameDictionary, sourceIntersectionName, destinationIntersectionName, True)
            else:
                #execute Diikstra's algorithm for single path1
                findShortestPathMultiple(adjacencyList, intersectionNameDictionary, sourceIntersectionName, destinationIntersectionName, False)
        userInput = input("Enter \"1\" to find a single shortest path, enter \"2\" to find multiple shortest paths, enter \"exit\" to exit: ")
    '''
