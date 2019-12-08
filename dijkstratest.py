from pathfinder.algorithms.dijkstra import findDijkstra
from pathfinder.types.graph import *

#gr = Graph("./graphs/test1.txt")
gr = Graph("./graphs/tree.txt")

#start = gr.get("node1")
#goal = gr.get("node3")

start = gr.get("root")
goal = gr.get("br3.1")

print(findDijkstra(start, goal))

backwalk = goal
while backwalk:
    print(backwalk)
    backwalk = backwalk.before
