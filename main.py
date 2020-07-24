import pygameMain
import safestPathAlg

#MAIN FUNCTION
import Mapinit

if __name__ == '__main__':
    #COMMAND MENU
    userInput = input("Enter \"1\" to begin a shortest-path search, enter \"2\" to configure options, enter \"exit\" to exit: ")
    while(userInput != "exit"):
        #enter algorithms-submenu
        if(userInput == "1"):
            #specify that the CSV file being used is the small size one
            Mapinit.mapFileName = Mapinit.smallMapFileName
            userInput = input("\nEnter \t\"1\" to perform visual GUI shortest-path search (small grid)\n\t\"2\" to perform text-based shortest path search (large grid)\n\t\"3\" to perform text-based multiple shortest paths search (large grid)\n\t\"cancel\" to return to the main menu\n(type in here): ")
            while(userInput != "1" and userInput != "2" and userInput != "3" and userInput != "cancel"):
                userInput = input("\nEnter \t\"1\" to perform visual GUI shortest-path search (small grid)\n\t\"2\" to perform text-based shortest path search (large grid)\n\t\"3\" to perform text-based multiple shortest paths search (large grid)\n\t\"cancel\" to return to the main menu\n(type in here): ")
            #single shortest path visual GUI function
            if(userInput == "1"):
                pygameMain.main_menu()
            #single shortest path text function command
            elif(userInput == "2"):
                #specify that the CSV file being used is the big size one
                Mapinit.mapFileName = Mapinit.bigMapFileName
                #first find the dimensions of the map
                rows, columns = safestPathAlg.findDimensionsOfMap()
                #load a new map & adjacency list instance
                array = safestPathAlg.createArray(rows, columns)
                adjacencyList, intersectionNameDictionary = safestPathAlg.createAdjacencyList(array, rows, columns)
                #receive user-input
                if(Mapinit.useNumbersInsteadOfStreetNames == False):
                    sourceIntersectionName = input("Enter name of starting street intersection (e.g. \"Chevrolet / Westbrooke\"): ")
                    destinationIntersectionName = input("Enter name of destination street intersection (e.g. \"Studebaker / Rochelle\"): ")
                else:
                    sourceIntersectionName = input("Enter name of starting street intersection (e.g. \"0 / 0\"): ")
                    destinationIntersectionName = input("Enter name of destination street intersection (e.g. \"1 / 1\"): ")
                weightMode = input("Factor in crime map? (\"y\") or find the strictly shortest physical path (\"n\")?: ")
                while(weightMode != "y" and weightMode != "n"):
                    weightMode = input("Factor in crime map? (\"y\") or find the strictly shortest physical path (\"n\")?: ")
                if(weightMode == "y"):
                    #execute Diikstra's algorithm for single path
                    safestPathAlg.findShortestPathSingle(adjacencyList, intersectionNameDictionary, sourceIntersectionName, destinationIntersectionName, True)
                else:
                    #execute Diikstra's algorithm for single path
                    safestPathAlg.findShortestPathSingle(adjacencyList, intersectionNameDictionary, sourceIntersectionName, destinationIntersectionName, False)
            #multiple shortest path text function command
            elif(userInput == "3"):
                #specify that the CSV file being used is the big size one
                Mapinit.mapFileName = Mapinit.bigMapFileName
                #first find the dimensions of the map
                rows, columns = safestPathAlg.findDimensionsOfMap()
                #receive user-input
                if(Mapinit.useNumbersInsteadOfStreetNames == False):
                    sourceIntersectionName = input("Enter name of starting street intersection (e.g. \"Chevrolet / Westbrooke\"): ")
                    destinationIntersectionName = input("Enter name of destination street intersection (e.g. \"Studebaker / Rochelle\"): ")
                else:
                    sourceIntersectionName = input("Enter name of starting street intersection (e.g. \"0 / 0\"): ")
                    destinationIntersectionName = input("Enter name of destination street intersection (e.g. \"1 / 1\"): ")
                weightMode = input("Factor in crime map? (\"y\") or find the strictly shortest physical path (\"n\")?: ")
                while(weightMode != "y" and weightMode != "n"):
                    weightMode = input("Factor in crime map? (\"y\") or find the st1ictly shortest physical path (\"n\")?: ")
                #load a new map & adjacency list instance
                array = safestPathAlg.createArray(rows, columns)
                adjacencyList, intersectionNameDictionary = safestPathAlg.createAdjacencyList(array, rows, columns)
                if(weightMode == "y"):
                    #execute Diikstra's algorithm for single path
                    safestPathAlg.findShortestPathMultiple(adjacencyList, intersectionNameDictionary, sourceIntersectionName, destinationIntersectionName, True)
                else:
                    #execute Diikstra's algorithm for single path1
                    safestPathAlg.findShortestPathMultiple(adjacencyList, intersectionNameDictionary, sourceIntersectionName, destinationIntersectionName, False)
        #enter options sub-menu
        elif(userInput == "2"):
            userInput = input("\nEnter\t\"1\" to enable street-names (e.g. \"Chevrolet / Wilson\"),\n\t\"2\" to enable index numbers as street names (e.g. \"0 / 0\"),\n\t\"cancel\" to cancel\n(type in here): ")
            while(userInput != "1" and userInput != "2" and userInput != "cancel"):
                userInput = input("\nEnter,\n\t\"1\" to enable street-names (e.g. \"Chevrolet / Wilson\"),\n\t\"2\" to enable indicies as street names (e.g. \"0 / 0\"),\n\t\"cancel\" to cancel\n(type in here): ")
            if(userInput == "1"):
                Mapinit.useNumbersInsteadOfStreetNames = False
            elif(userInput == "2"):
                Mapinit.useNumbersInsteadOfStreetNames = True
        #loop for the main menu
        userInput = input("\nEnter \"1\" to begin a shortest-path search, enter \"2\" to configure options, enter \"exit\" to exit: ")
