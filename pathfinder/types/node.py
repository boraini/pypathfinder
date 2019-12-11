from pathfinder.types.path import *
from math import sqrt
class Node():
    def __init__(self, name):
        self.name = name
        self.paths = []
        self.cost = 1e7
        self.heuristic = 1e7
        self.x = 0
        self.y = 0
        self.before = None
    def __str__(self):
        out = ""
        for path in self.paths:
            out = out + str(path)
        return "Node " + self.name + " has paths to " + out
    def distPyth(self, nd):
        return sqrt((nd.x - self.x)(nd.x - self.x) + (nd.y - self.y)(nd.y - self.y))
    def distManh(self, nd):
        return abs(nd.x - self.x) + abs(nd.y - self.y)
    def distOcto(self, nd):
        return max(abs(nd.x - self.x), abs(nd.y - self.y))
    def addPath(self, target, cost):
        self.paths.append(Path(target, cost))
    def clear(self):
        self.cost = 1e7
        self.before = None

    def __lt__(self, other):
        return self.heuristic + self.cost < other.heuristic + other.cost
