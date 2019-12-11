from pathfinder.algorithms.dijkstra import findDijkstra
from pathfinder.types.graph import *
from timeit import timeit

gr = Graph("./graphs/rm2019basic.txt")

start = gr.get("1")
goal = gr.get("8")

def findDijkstraCaller():
    gr.clear()
    findDijkstra(start, goal)

t = timeit(findDijkstraCaller, number=1000)

print("Execution took: " + str(t))

backwalk = goal
while backwalk:
    print(backwalk)
    backwalk = backwalk.before
