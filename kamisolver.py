import xml.etree.ElementTree as ET
import numpy as np
from collections import Counter
from Node import Node
from State import State

# parse xml file to colormap
tree = ET.parse('TestFiles/SAL9_Targets.xml')
root = tree.getroot()

width = int(root.get('width'))
height = int(root.get('height'))
colmapString = ' '.join(root.get('colours'))

colmapArray = np.fromstring(colmapString, dtype=int, sep=' ')
colmap = colmapArray.reshape((height, width))

# parse colormap to graph
parsedMap = np.array([0] * height * width).reshape((height, width))
startingNeighborGrids = []
nodeGrids = []
graph = [] # all the nodes (patches) on graph

for y in range(height):
    for x in range(width):
        color = colmap[y,x]
        if parsedMap[y,x] == 0:
            node = Node(len(graph), color, [(y,x)], [])
            currentNodeGrids = []
            neighborGrids = []
            
            q = [(y,x)]
            while q:
                current = q.pop(0)
                cy = current[0]
                cx = current[1]
                for coord in [(cy, cx),(cy-1,cx),(cy,cx-1),(cy+1,cx),(cy,cx+1)]:
                    if -1 < coord[0] < height and -1 < coord[1] < width:
                        if colmap[coord] == color:
                            if not coord in currentNodeGrids:
                                currentNodeGrids.append(coord)
                                parsedMap[coord] = len(graph)
                                q.append(coord)
                        else:
                            if not coord in neighborGrids:
                                neighborGrids.append(coord)
            nodeGrids.append(currentNodeGrids)
            startingNeighborGrids.append(neighborGrids)
            graph.append(node)

# link nodes to each other
for startNode in graph:
    for grid in startingNeighborGrids[startNode.id]:
        for endNode in graph:
            if grid in nodeGrids[endNode.id]:
                startNode.appendNeighborNode(endNode.id)

# Calculate heuristic value for each node's each potential move.
# H = N - C
# H: Heuristic Value, moves with higher heuristic value get searched first
# N: Number of target colored neighbor nodes 
# TODO: C: The gretest distance to other node (eccentricity)

# Generate a list of all possible moves with heuristic valueH = N
# [(node id, target color, H)]
moves = []
for node in graph:
    # count the number of neighbors in each color, then sort by count
    colorCount = Counter([graph[x].color for x in node.neighborNodes]).most_common()
    for item in colorCount:
        move = [node.id, item[0], item[1]]
        moves.append(move)
moves.sort(key=lambda x: x[2], reverse=True)
print moves

# Make a DFS search to find an optimal solution.
# Keep track of the solution with the minimum steps,
# prune the branches that's deeper than the shortest solution so far.
stateStack = []










