class Node:
    def __init__(self, nodeid, color, coordl, neighborn):
        self.id = nodeid # int
        self.color = color # int
        self.coordlist = coordl #[[y,x]]
        self.neighborNodes = neighborn #[list of neighbor id]

    def appendCoord(self, coord):
        if not coord in self.coordlist:
            self.coordlist.append(coord)

    def appendNeighborNode(self, node):
        if not node in self.neighborNodes:
            self.neighborNodes.append(node)

    def write(self):
        print "id: ", self.id
        print "color: ", self.color
        print "coordlist", self.coordlist
        print "neighborNodes: ", self.neighborNodes