from pathfinder.algorithms.aStar import findAStar
from pathfinder.algorithms.dijkstra import findDijkstra
from pathfinder.types.graph import *
from timeit import timeit

gr = Graph("graphs/grid.txt")

start = gr.get("1,1")
goal = gr.get("18,13")

def findAStarCaller():
    gr.clear()
    findAStar(start, goal)

t = timeit(findAStarCaller, number=1)


def findDijkstraCaller():
    gr.clear()
    findDijkstra(start, goal)

t = timeit(findDijkstraCaller, number=1)

print("Operation time: %g" % (t))
gr.clear()
ret = findAStar(start, goal)
print("Operation cost: %d" % (ret[0]))
print("Operation count: %d" % (ret[1]))
backwalk = goal
while backwalk:
    print(backwalk)
    backwalk = backwalk.before

print("\n\n\n\n\n\n\n\n\n")

print("Operation time: %g" % (t))
gr.clear()
ret = findDijkstra(start, goal)
print("Operation cost: %d" % (ret[0]))
print("Operation count: %d" % (ret[1]))
backwalk = goal
while backwalk:
    print(backwalk)
    backwalk = backwalk.before
