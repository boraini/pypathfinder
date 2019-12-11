from pathfinder.types.node import Node
from pathfinder import util
from queue import PriorityQueue
import heapq



def findAStar(start, goal):
    open = [start]
    heapq.heapify(open)
    start.cost = 0
    start.heuristic = start.distManh(goal)
    start.before = None
    while len(open) > 0:
        current = heapq.heappop(open)
        for path in current.paths:
            newcost = current.cost + path.cost
            target = path.target
            if (target is goal):
                target.cost = newcost
                target.before = current
                break
            if (newcost < target.cost):
                heapq.heappush(open, path.target)
                target.heuristic = target.distManh(goal)
                target.before = current
                target.cost = newcost
    return goal.cost

# def nextPrior(ls, func):
#     mostprior = 0
#     priority = func(ls[mostprior])
#     for i in range(len(ls)):
#         newpriority = func(ls[i])
#         if newpriority > priority:
#             mostprior = i
#             priority = newpriority
#     return ls.pop(mostprior)
