import xml.etree.ElementTree as ET
import numpy
from Node import Node


def parse_color_map(filepath):
    # parse xml file to colormap
    tree = ET.parse(filepath)
    root = tree.getroot()

    width = int(root.get('width'))
    height = int(root.get('height'))
    colormap_string = ' '.join(root.get('colours'))

    colormap_array = numpy.fromstring(colormap_string, dtype=int, sep=' ')
    colormap = colormap_array.reshape(height, width)
    return colormap


def parse_to_graph(colormap):
    # parse colormap to graph
    height = len(colormap)
    width = len(colormap[0])
    parsed_map = numpy.array([0] * height * width).reshape((height, width))
    starting_neighbor_grids = []
    starting_node_grids = []
    graph = []  # all the nodes (patches) on graph

    for y in range(height):
        for x in range(width):
            color = colormap[y, x]
            if parsed_map[y, x] == 0:
                node = Node(len(graph), color, [(y, x)], [])
                current_node_grids = set()
                neighbor_grids = []

                q = [(y, x)]
                while q:
                    current = q.pop(0)
                    cy = current[0]
                    cx = current[1]
                    for coord in [(cy, cx), (cy - 1, cx), (cy, cx - 1), (cy + 1, cx), (cy, cx + 1)]:
                        if -1 < coord[0] < height and -1 < coord[1] < width:
                            if colormap[coord] == color:
                                if coord not in current_node_grids:
                                    current_node_grids.add(coord)
                                    parsed_map[coord] = len(graph)
                                    q.append(coord)
                            else:
                                if coord not in neighbor_grids:
                                    neighbor_grids.append(coord)
                starting_node_grids.append(current_node_grids)
                starting_neighbor_grids.append(neighbor_grids)
                graph.append(node)

    # link nodes to each other
    for startNode in graph:
        for grid in starting_neighbor_grids[startNode.id]:
            for endNode in graph:
                if grid in starting_node_grids[endNode.id]:
                    startNode.append_neighbor_nodes(endNode.id)
