import safestPathAlg
#MAIN FUNCTION
if __name__ == '__main__':
    #first find the dimensions of the map
    rows, columns = safestPathAlg.findDimensionsOfMap()
    #COMMAND MENU
    userInput = input("Enter \"1\" to find a single shortest path, enter \"2\" to find multiple shortest paths, enter \"exit\" to exit: ")
    while(userInput != "exit"):
        #if the command was one of the cardinal directions, see if you can move there
        #and if you can, then move there
        #if you can't then stay where you were
        if(userInput == "1"):
            sourceIntersectionName = input("Enter name of starting street intersection (e.g. \"Baker / Wilson\": ")
            destinationIntersectionName = input("Enter name of destination street intersection (e.g. \"Chevrolet / Sushi\"): ")
            weightMode = input("Factor in crime map? (\"y\") or find the strictly shortest physical path (\"n\")?: ")
            while(weightMode != "y" and weightMode != "n"):
                weightMode = input("Factor in crime map? (\"y\") or find the strictly shortest physical path (\"n\")?: ")
            #load the map
            adjacencyList, intersectionNameDictionary = safestPathAlg.createAdjacencyList(rows, columns)
            if(weightMode == "y"):
                #execute Diikstra's algorithm for single path
                safestPathAlg.findShortestPathSingle(adjacencyList, intersectionNameDictionary, sourceIntersectionName, destinationIntersectionName, True)
            else:
                #execute Diikstra's algorithm for single path
                safestPathAlg.findShortestPathSingle(adjacencyList, intersectionNameDictionary, sourceIntersectionName, destinationIntersectionName, False)
        elif(userInput == "2"):
            sourceIntersectionName = input("Enter name of starting street intersection (e.g. \"Baker / Wilson\"): ")
            destinationIntersectionName = input("Enter name of destination street intersection (e.g. \"Chevrolet / Sushi\"): ")
            weightMode = input("Factor in crime map? (\"y\") or find the strictly shortest physical path (\"n\")?: ")
            while(weightMode != "y" and weightMode != "n"):
                weightMode = input("Factor in crime map? (\"y\") or find the strictly shortest physical path (\"n\")?: ")
            #load the map
            adjacencyList, intersectionNameDictionary = safestPathAlg.createAdjacencyList(rows, columns)
            if(weightMode == "y"):
                #execute Diikstra's algorithm for single path
                safestPathAlg.findShortestPathMultiple(adjacencyList, intersectionNameDictionary, sourceIntersectionName, destinationIntersectionName, True)
            else:
                #execute Diikstra's algorithm for single path
                safestPathAlg.findShortestPathMultiple(adjacencyList, intersectionNameDictionary, sourceIntersectionName, destinationIntersectionName, False)
        userInput = input("Enter \"1\" to find a single shortest path, enter \"2\" to find multiple shortest paths, enter \"exit\" to exit: ")
