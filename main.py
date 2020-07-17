import Mapinit
import safestPathAlg



if __name__ == '__main__':
    #first find the dimensions of the map
    rows, columns = safestPathAlg.findDimensionsOfMap()

    ##call function to create map and store the single returned node from which the rest of the graph can be accessed
    #createdGraph = createMapAsNodes(rows, columns)
    ##debugging explore graph function to see if graph was linked correctly between its nodes
    #exploreGraphAsNodes(createdGraph)

    #create 2-D list adjacency list of the map
    adjacencyList = safestPathAlg.createMapAsAdjacencyList(rows, columns)



    #1st row ("1st as in not the programming type of 1"), 1st column to 9th row, 8th column
    #findShortestPathAdjacencyList(adjacencyList, "Chevrolet", "Oldsmobile", "Porsche","Eustace")
    safestPathAlg.findShortestPathAdjacencyList(adjacencyList, 0, 0, 8, 7)

    #reload the map
    adjacencyList = safestPathAlg.createMapAsAdjacencyList(rows, columns)
    #2nd row, 2nd column
    #findShortestPathAdjacencyList(adjacencyList, "Chevrolet", "Oldsmobile", "Studebaker","Fiat")
    safestPathAlg.findShortestPathAdjacencyList(adjacencyList, 0, 0, 1, 1)
