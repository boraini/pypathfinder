from pathfinder.algorithms.aStar import findAStar
from pathfinder.types.graph import *
from timeit import timeit

gr = Graph("./graphs/rm2019basic.txt")

start = gr.get("1")
goal = gr.get("20")

def findAStarCaller():
    gr.clear()
    findAStar(start, goal)

t = timeit(findAStarCaller, number=1000)

print("Operation time: %g" % (t))
gr.clear()
ret = findAStar(start, goal)
print("Operation cost: %d" % (ret[0]))
print("Operation count: %d" % (ret[1]))

backwalk = goal
while backwalk:
    print(backwalk)
    backwalk = backwalk.before
