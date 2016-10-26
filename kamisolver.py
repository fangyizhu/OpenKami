import xml.etree.ElementTree as ET
import numpy as np
from collections import Counter
from Node import Node


# Calculate heuristic value for each node's each potential move.
# H = N - C
# H: Heuristic Value, moves with higher heuristic value get searched first
# N: Number of target colored neighbor nodes 
# TODO: C: The gretest distance to other node (eccentricity)

# Generate a list of all possible moves with heuristic valueH = N
# [list of [node id, target color, H, index in graphStates]]
graphStates = [graph] # store up each inital state of the moves

def generate_next_moves(state_id):
    moves = []
    currentGraph = graphStates[state_id]
    for node in currentGraph:
        # count the number of neighbors in each color, then sort by count
        colorCount = Counter([currentGraph[x].color for x in node.neighborNodes]).most_common()
        for item in colorCount:
            move = [node.id, item[0], item[1], state_id]
            moves.append(move)
    moves.sort(key=lambda x: x[2], reverse=True)
    return moves

# Make a DFS search to find an optimal solution.
# Keep track of the solution with the minimum steps,
# prune the branches that's deeper than the shortest solution so far.

moveStack = [] # [stack of [node id, target color, H, index in graphStates]]
