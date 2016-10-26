class Node:
    def __init__(self, nodeid, color, coord, neighbors):
        self.id = nodeid
        self.color = color
        self.coord = coord
        self.neighborNodes = neighbors

    def append_neighbor_nodes(self, node):
        if node not in self.neighborNodes:
            self.neighborNodes.append(node)

    def write(self):
        print("id: ", self.id)
        print("color: ", self.color)
        print("coord", self.coord)
        print("neighborNodes: ", self.neighborNodes)