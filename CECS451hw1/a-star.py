import heapq

def shortest_path(start, end, graph):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, current) = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        if current == end:
            return cost
        for neighbor in graph[current]:
            heapq.heappush(heap, (cost + haversine_distance(current[0], current[1], neighbor[0], neighbor[1]), neighbor))
    return float('inf')

# Example usage
graph = {
    (51.5074, 0.1278): [(40.7128, -74.0060), (37.7749, -122.4194)],
    (40.7128, -74.0060): [(51.5074, 0.1278), (37.7749, -122.4194)],
    (37.7749, -122.4194): [(51.5074, 0.1278), (40.7128, -74.0060)],
}
print(shortest_path((51.5074, 0.1278), (37.7749, -122.4194), graph)) # Output: 5567.255534548576
''' writing down thoughts so that i remember in the morning

need to convert cities in the dictionary to their coordinates? similar to how they use the coordinates in the above example


'''


# import sys
# import heapq
# import math
# import queue

# def read_map(filename):
#     with open(filename, 'r') as f:
#         map_data = {}
#         for line in f:
#             split_line = line.strip().split('-')
#             city = split_line[0].strip()
#             neighbors_and_distances = split_line[1].strip().split(',')
#             map_data[city] = [(neighbor.strip(), float(distance.strip())) for neighbor, distance in [neighbor_and_distance.strip().strip(')').split('(') for neighbor_and_distance in neighbors_and_distances]]
#             # for neighbor_and_distance in neighbors_and_distances:
#             #     neighbor_and_distance = neighbor_and_distance.strip().strip(')').split('(')
#             #     print(neighbor_and_distance)
#             #     for neighbor, distance in neighbor_and_distance:
#             #         print(neighbor, distance)
#             #         map_data[city] = (neighbor.strip(), float(distance.strip()))
#         # map_data = {}
#         # for line in f:
#         #     line = line.split('-')
#         #     line[1] = line[1].split(',')
#         #     for item in line[1]:
#         #         item = item.strip().strip(')').split('(')
#         #         item = (item[0], item[1])
#         #         map_data[line[0]] = item
#         # print (map_data['SanFrancisco'])
#         #map_data = {line.split(':')[0].strip(): [(neighbor.strip(), int(distance.strip()[1:-1])) for neighbor, distance in [neighbor_and_distance.strip().split('(') for neighbor_and_distance in line.split(':')[1].split(',')]] for line in f}
#         #map_data = {line.split(':')[0]: [(neighbor, int(distance.strip(')'))) for neighbor, distance in (neighbor_and_distance.split('(') for neighbor_and_distance in line.split(':')[1].split(','))] for line in f}
#         #map_data = {line.split()[0]: [(neighbor, int(distance)) for neighbor, distance in (neighbor_and_distance.split(',') for neighbor_and_distance in line.split()[2:])] for line in f}
#     return map_data

# def read_coordinates(filename):
#     with open(filename, 'r') as f:
#         coordinate_data = []
#         for line in f.readlines():
#             line = line.split(':')
#             line[1] = line[1].strip().strip('(').strip(')').split(',')
#             coordinate_data.append((line[0], line[1][0], line[1][1]))
#     coordinates = {city: (float(lat), float(long)) for city, lat, long in coordinate_data}
#     return coordinates

# def HaversineEstimateCost(startLatitude, startLongitude, goalLatitude, goalLongitude):
#     startLatitude, startLongitude, goalLatitude, goalLongitude = map(math.radians, [startLatitude, startLongitude, goalLatitude, goalLongitude])
#     return 2 * 3958.8 * math.sinh(math.sqrt((math.sin((goalLatitude - startLatitude)/2))**2 + math.cos(startLatitude) 
#             * math.cos(goalLatitude) * (math.sin((goalLongitude-startLongitude)/2)**2)))

# # def haversine_distance(lat1, long1, lat2, long2):
# #     R = 3958.8 # earth's radius in miles
# #     lat1, long1, lat2, long2 = map(math.radians, [lat1, long1, lat2, long2])
# #     dlat = lat2 - lat1
# #     dlong = long2 - long1
# #     a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlong / 2)**2
# #     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
# #     return R * c

# # def a_star(graph, start, goal):
# #     frontier = PriorityQueue()
# #     frontier.put(start, 0)
# #     came_from = {}
# #     cost_so_far = {}
# #     came_from[start] = None
# #     cost_so_far[start] = 0
# #     cities = []

# #     while not frontier.empty():
# #         current = frontier.get()

# #         if current == goal:
# #             break

# #         for next_city, actual_distance in graph[current].items():
# #             new_cost = cost_so_far[current] + actual_distance
# #             if next_city not in cost_so_far or new_cost < cost_so_far[next_city]:
# #                 cost_so_far[next_city] = new_cost
# #                 priority = new_cost + HaversineEstimateCost(coordinates[current], coordinates[next_city])
# #                 frontier.put(next_city, priority)
# #                 came_from[next_city] = current

# #     return came_from, cost_so_far

# def a_star(start, goal, map_data, coordinates):
#     heap = [(0, start)]
#     visited = set()
#     while heap:
#         (cost, current) = heapq.heappop(heap)
#         if current == goal:
#             return cost
#         if current in visited:
#             continue
#         visited.add(current)
#         for (neighbor, distance) in map_data[current]:
#             if neighbor in visited:
#                 continue
#             lat1, long1 = coordinates[current]
#             lat2, long2 = coordinates[neighbor]
#             heapq.heappush(heap, (cost + HaversineEstimateCost(lat1, long1, lat2, long2), neighbor))
#     return float('inf')

# if __name__ == '__main__':
#     start = sys.argv[1]
#     goal = sys.argv[2]
#     map_data = read_map('map.txt')
#     coordinates = read_coordinates('coordinates.txt')
#     cost = a_star(start, goal, map_data, coordinates)
#     print(f'The fastest route from {start} to {goal} has a cost of {cost} miles.')



# # import heapq
# # import math

# # mapFile = open(r"C:\Users\jakes\Documents\CECS451\CECS451hw1\map.txt")
# # mapDict = {}
# # actualDistances = {}
# # for line in mapFile:
# #     line = line.strip()
# #     tempNeighborsList = line.split('-')[1].split(',')
# #     # for neighbor in tempNeighborsList:
# #     #     neighbor = neighbor.split('(')
# #     #     neighbor[1] = neighbor[1].strip(')')
# #     #     actualDistances[neighbor[0]] = neighbor[1]
        
# #     for i in range(len(tempNeighborsList)):
# #         neighbor = tempNeighborsList[i].split('(')
# #         tempNeighborsList[i] = neighbor[0]
# #         actualDistances[tempNeighborsList[i]] = neighbor[1].strip(')')
    
# #     mapDict[line.split('-')[0]] = tempNeighborsList
# #     #print([line.split('-')[0].split('(')[0]])
# # mapFile.close()

# # coordinatesFile = open(r"C:\Users\jakes\Documents\CECS451\CECS451hw1\coordinates.txt")
# # coordinates = {}
# # for line in coordinatesFile:
# #     line = line.strip()
# #     line = line.strip(')')
# #     line = line.replace('(', '')
# #     coordinates[line.split(':')[0]] = line.split(':')[1].split(',')
# # coordinatesFile.close()

# # def HaversineEstimateCost(startLatitude, startLongitude, goalLatitude, goalLongitude):
# #     startLatitude, startLongitude, goalLatitude, goalLongitude = map(math.radians, [startLatitude, startLongitude, goalLatitude, goalLongitude])
# #     return 2 * 3958.8 * math.sinh(math.sqrt((math.sin((goalLatitude - startLatitude)/2))**2 + math.cos(startLatitude) 
# #             * math.cos(goalLatitude) * (math.sin((goalLongitude-startLongitude)/2)**2)))

# # def a_star(start, goal, map):
# #     heap = [(0, start)]
# #     visited = set()
# #     while heap:
# #         (cost, current) = heapq.heappop(heap)
# #         if current == goal:
# #             return cost
# #         if current in visited:
# #             continue
# #         visited.add(current)
# #         for neighbor in map[current]:
# #             heuristic = HaversineEstimateCost(float(coordinates[current][0]), float(coordinates[current][1]), 
# #                 float(coordinates[goal][0]), float(coordinates[goal][1]))
# #             # heuristic = HaversineEstimateCost(float(coordinates[current][0]), float(coordinates[current][1]), 
# #             #     float(coordinates[neighbor][0]), float(coordinates[neighbor][1]))
# #             heapq.heappush(heap, (cost + float(actualDistances[neighbor]) + heuristic, neighbor))
# #     return float("inf")
    
    
# #     # heap = [(0, start)]
# #     # visited = set()
# #     # while heap:
# #     #     (cost, current) = heapq.heappop(heap)
# #     #     if current in visited:
# #     #         continue
# #     #     visited.add(current)
# #     #     if current == goal:
# #     #         return cost
# #     #     for neighbor in map[current]:
# #     #         if neighbor in visited:
# #     #             continue
# #     #         estimated_cost = HaversineEstimateCost(float(coordinates[neighbor][0]), float(coordinates[neighbor][1]), 
# #     #             float(coordinates[goal][0]), float(coordinates[goal][1]))
# #     #         heapq.heappush(heap, (cost + float(actualDistances[neighbor]) + estimated_cost, neighbor))
# #     #         print(neighbor)
# #     # return float("inf")
    
# #     # heap = [(0, start)]
# #     # visited = set()
# #     # while heap:
# #     #     (cost, current) = heapq.heappop(heap)
# #     #     if current == goal:
# #     #         return cost
# #     #     if current in visited:
# #     #         continue
# #     #     visited.add(current)
# #     #     print(current)
# #     #     for neighbor in map[current]:
# #     #         print(*coordinates[neighbor])
# #     #         #estimated_cost = HaversineEstimateCost(float(*coordinates[neighbor]), float(*coordinates[goal]))
# #     #         heapq.heappush(heap, (cost + float(actualDistances[neighbor]), neighbor))
# #     #         # heapq.heappush(heap, (cost + 1 + HaversineEstimateCost((float(coordinates[current][0]))*(math.pi/180), #take out the +1???
# #     #         #     (float(coordinates[current][1]))*(math.pi/180), (float(coordinates[neighbor][0]))*(math.pi/180), 
# #     #         #     (float(coordinates[neighbor][1]))*(math.pi/180)), neighbor))
# #     # return float('inf')
# #     # print("From city: " + start + "\nTo city: " + goal + "\nBest Route: " 
# #     #     + #best route
# #     #     + "\nTotal distance: " + a_star(start, goal, graph))

# # # Example usage
# # graph = {'A': ['B', 'C', 'D'],
# #          'B': ['A', 'E', 'F'],
# #          'C': ['A', 'G'],
# #          'D': ['A'],
# #          'E': ['B'],
# #          'F': ['B'],
# #          'G': ['C']}
# # start = 'SanFrancisco'
# # goal = 'LongBeach'
# # print("From city: " + str(start) + "\nTo city: " + str(goal) + "\nBest Route: " 
# #         + ""#best route
# #         + "\nTotal distance: " + str(a_star(start, goal, mapDict)))
