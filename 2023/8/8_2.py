import os
import sys
import math

with open(os.path.join(sys.path[0], "input.txt")) as f:
    instructions, nodes = f.read().split("\n\n")
    instructions = instructions.replace("L", "0")
    instructions = instructions.replace("R", "1")
    nodes = [node.split(" = ") for node in nodes.split("\n")]
    paths = {}
    for node in nodes:
        node[1] = node[1].replace("(", "")
        node[1] = node[1].replace(")", "")
        paths[node[0]] = tuple(node[1].split(", "))

    idx = 0
    current_nodes = [node for node in paths.keys() if node[-1] == "A"]
    steps = 0

    min_steps = [0] * len(current_nodes)

    while 0 in min_steps:
        for i, node in enumerate(current_nodes):
            if node[-1] == "Z" and min_steps[i] == 0:
                min_steps[i] = steps

        current_nodes = [paths[node][int(instructions[idx])]
                         for node in current_nodes]

        idx = (idx+1) % len(instructions)
        steps += 1

    print(math.lcm(*min_steps))
