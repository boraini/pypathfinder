from pathfinder.algorithms.aStar import findAStar
from pathfinder.types.graph import *
from timeit import timeit

gr = Graph("./graphs/rm2019basic.txt")

start = gr.get("14")
goal = gr.get("7")

def findAStarCaller():
    gr.clear()
    findAStar(start, goal)

t = timeit(findAStarCaller, number=1000)

print("Execution took: " + str(t))

backwalk = goal
while backwalk:
    print(backwalk)
    backwalk = backwalk.before
