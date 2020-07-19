import safestPathAlg

# MAIN FUNCTION
if __name__ == '__main__':
    # first find the dimensions of the map
    rows, columns = safestPathAlg.findDimensionsOfMap()
    # create 2-D list adjacency list of the map
    adjacencyList, intersectionNameDictionary = safestPathAlg.createAdjacencyList(rows, columns)

    # for i in range(len(adjacencyList)):
    #    print("Row", i,":", end="")
    #    for j in range(len(adjacencyList[i].adjacentNodes)):
    #        print(adjacencyList[i].adjacentNodes[j].intersectionName, " --- ", end="")
    #    print()
    # for i in intersectionNameDictionary:
    #   print(i, "--->", intersectionNameDictionary[i])

    # test
    safestPathAlg.findShortestPathAdjacencyList(adjacencyList, intersectionNameDictionary, "0 / 0", "4 / 3", True)
    # reload the map
    adjacencyList, intersectionNameDictionary = safestPathAlg.createAdjacencyList(rows, columns)
    safestPathAlg.findShortestPathAdjacencyList(adjacencyList, intersectionNameDictionary, "0 / 0", "4 / 3", False)
