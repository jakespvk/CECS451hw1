import heapq

mapFile = open(r"C:\Users\jakes\Documents\CECS451\CECS451hw1\map.txt")
map = {}
for i in range(18):
    mapLine = str(mapFile.readline)
    print(mapLine)
    map[mapLine.split('-')[0]] = (mapLine.split('-')[1].split(','))

def a_star(start, goal, graph):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, current) = heapq.heappop(heap)
        if current == goal:
            return cost
        if current in visited:
            continue
        visited.add(current)
        for neighbor in graph[current]:
            heapq.heappush(heap, (cost + 1, neighbor))
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
start = 'A'
goal = 'F'
print("From city: " + str(start) + "\nTo city: " + str(goal) + "\nBest Route: " 
        + ""#best route
        + "\nTotal distance: " + str(a_star(start, goal, graph)))
