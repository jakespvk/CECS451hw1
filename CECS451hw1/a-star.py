import heapq
import math

mapFile = open(r"C:\Users\jakes\Documents\CECS451\CECS451hw1\map.txt")
map = {}
actualDistances = {}
for line in mapFile:
    line = line.strip()
    tempNeighborsList = line.split('-')[1].split(',')
    # for neighbor in tempNeighborsList:
    #     neighbor = neighbor.split('(')
    #     neighbor[1] = neighbor[1].strip(')')
    #     actualDistances[neighbor[0]] = neighbor[1]
        

    for i in range(len(tempNeighborsList)):
        neighbor = tempNeighborsList[i].split('(')
        tempNeighborsList[i] = neighbor[0]
        actualDistances[tempNeighborsList[i]] = neighbor[1].strip(')')
        print(actualDistances[tempNeighborsList[i]])
    
    map[line.split('-')[0]] = tempNeighborsList
    #print([line.split('-')[0].split('(')[0]])
mapFile.close()

coordinatesFile = open(r"C:\Users\jakes\Documents\CECS451\CECS451hw1\coordinates.txt")
coordinates = {}
for line in coordinatesFile:
    line = line.strip()
    line = line.strip(')')
    line = line.replace('(', '')
    coordinates[line.split(':')[0]] = line.split(':')[1].split(',')
coordinatesFile.close()

def HaversineEstimateCost(startLatitude, startLongitude, goalLatitude, goalLongitude):
    return 2 * 3958.8 * math.sinh(math.sqrt((math.sin((goalLatitude - startLatitude)/2))**2 + math.cos(startLatitude) 
            * math.cos(goalLatitude) * (math.sin((goalLongitude-startLongitude)/2)**2)))

def a_star(start, goal, map):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, current) = heapq.heappop(heap)
        if current == goal:
            return cost
        if current in visited:
            continue
        visited.add(current)
        for neighbor in map[current]:
            heapq.heappush(heap, (cost + 1 + HaversineEstimateCost((float(coordinates[current][0]))*(math.pi/180), #take out the +1???
                (float(coordinates[current][1]))*(math.pi/180), (float(coordinates[neighbor][0]))*(math.pi/180), 
                (float(coordinates[neighbor][1]))*(math.pi/180)), neighbor))
    return float('inf')
    print("From city: " + start + "\nTo city: " + goal + "\nBest Route: " 
        + #best route
        + "\nTotal distance: " + a_star(start, goal, graph))

# Example usage
graph = {'A': ['B', 'C', 'D'],
         'B': ['A', 'E', 'F'],
         'C': ['A', 'G'],
         'D': ['A'],
         'E': ['B'],
         'F': ['B'],
         'G': ['C']}
start = 'SanFrancisco'
goal = 'LongBeach'
print("From city: " + str(start) + "\nTo city: " + str(goal) + "\nBest Route: " 
        + ""#best route
        + "\nTotal distance: " + str(a_star(start, goal, map)))
