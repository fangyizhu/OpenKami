class Node:
    def __init__(self, nodeid, color, coord, neighborn):
        self.id = nodeid # int
        self.color = color # int
        self.coord = coord # [(y,x)]
        self.neighborNodes = neighborn #[list of neighbor id]

    def appendNeighborNode(self, node):
        if not node in self.neighborNodes:
            self.neighborNodes.append(node)

    def write(self):
        print "id: ", self.id
        print "color: ", self.color
        print "coord", self.coord
        print "neighborNodes: ", self.neighborNodes