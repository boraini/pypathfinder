import pathfinder.types.node
from pathfinder import util
def findDijkstra(start, goal):
    start.cost = 0
    start.before = None
    open = [start]
    closed = []
    while len(open) > 0:
        current = open[0]
        for path in current.paths:
            newcost = current.cost + path.cost
            if (newcost < path.target.cost):
                open.append(path.target)
                path.target.before = current
                path.target.cost = newcost
                if (util.inRef(closed, path.target)):
                    util.removeRef(closed, path.target)
        util.removeRef(open, current)
        closed.append(current)
    return goal.cost
