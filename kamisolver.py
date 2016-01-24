import xml.etree.ElementTree as ET
import numpy as np
from collections import Counter

# parse xml file to colormap
tree = ET.parse('TestFiles/SAL9_Targets.xml')
root = tree.getroot()

width = int(root.get('width'))
height = int(root.get('height'))
colmapString = ' '.join(root.get('colours'))

colmapArray = np.fromstring(colmapString, dtype=int, sep=' ')
colmap = colmapArray.reshape((height, width))
print colmap

class Node:
    def __init__(self, nodeid, color, coordl, neighborn, neighborg):
        self.id = nodeid # int
        self.color = color # int
        self.coordlist = coordl #[[y,x]]
        self.neighborNodes = neighborn #[list of neighbor id]
        self.neighborGrids = neighborg #[[y,x]]

    def appendCoord(self, coord):
        if not coord in self.coordlist:
            self.coordlist.append(coord)

    def appendNeighborNode(self, node):
        if not node in self.neighborNodes:
            self.neighborNodes.append(node)

    def appendNeighborGrid(self, grid):
        if not grid in self.neighborGrids:
            self.neighborGrids.append(grid)

    def write(self):
        print "id: ", self.id
        print "color: ", self.color
        print "coordlist", self.coordlist
        print "neighborNodes: ", self.neighborNodes
        print "neighborGrids: ", self.neighborGrids

# parse colormap to graph
parsedMap = np.array([0] * height * width).reshape((height, width))
nodes = [] # all the nodes (patches) on graph

for y in range(height):
    for x in range(width):
        color = colmap[y,x]
        if parsedMap[y,x] == 0:
            node = Node(len(nodes), color, [(y,x)], [], [])
            q = [(y,x)]
            while q:
                current = q.pop(0)
                cy = current[0]
                cx = current[1]
                for coord in [(cy-1,cx),(cy,cx-1),(cy+1,cx),(cy,cx+1)]:
                    if -1 < coord[0] < height and -1 < coord[1] < width:
                        if colmap[coord] == color:
                            if not coord in node.coordlist:
                                node.appendCoord(coord)
                                parsedMap[coord] = 1
                                q.append(coord)
                        else:
                            node.appendNeighborGrid(coord)

            nodes.append(node)

# link nodes to each other
for startNode in nodes:
    for grid in startNode.neighborGrids:
        for endNode in nodes:
            if grid in endNode.coordlist:
                startNode.appendNeighborNode(endNode.id)

# Calculate heuristic value for each node's each potential move.
# H = N - C
# H: Heuristic Value, moves with higher heuristic value get searched first
# N: Number of target colored neighbor nodes 
# TODO: C: The gretest distance to other node (eccentricity)

# Generate a list of all possible moves with heuristic valueH = N
# [(node id, target color, H)]
moves = []
for node in nodes:
    # count the number of neighbors in each color, then sort by count
    colorCount = Counter([nodes[x].color for x in node.neighborNodes]).most_common()
    for item in colorCount:
        move = [node.id, item[0], item[1]]
        moves.append(move)
moves.sort(key=lambda x: x[2], reverse=True)
print moves











