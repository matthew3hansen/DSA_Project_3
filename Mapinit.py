# Initalizations
#mapFileName = "Csv-Files/randomizedMapWithLights.csv"
#mapFileName = "Csv-Files/randomizedCityMap.csv"
mapFileName = "Csv-Files/small_grid.csv"
streetNamesFileName = "Csv-Files/streetNames.csv"
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
        #boolean flag indicating that the Node has been visited for Dijikstra
        self.visited = False
        #storing the path(s) used for Dijikstra
        self.previousPath = []