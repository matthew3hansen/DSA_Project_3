# Initalizations
bigMapFileName = "Csv-Files/randomizedCityMap.csv"
smallMapFileName = "Csv-Files/small_grid.csv"
streetNamesFileName = "Csv-Files/streetNames.csv"
mapFileName = smallMapFileName #keep this as the smaller map name, as this default value is the one that is imported into by the pygames file
useNumbersInsteadOfStreetNames = True

#unsafeIntersectionWeight = 10
#safeIntersectionWeight = 1

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
        #visited flag used for the multiple-path version of Dijikstra
        self.visited = False
