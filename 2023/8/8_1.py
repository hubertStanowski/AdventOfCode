import os
import sys

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

    result = 0
    current_node = "AAA"

    while current_node != "ZZZ":
        idx = int(instructions[result % len(instructions)])
        current_node = paths[current_node][idx]
        result += 1

    print(result)
