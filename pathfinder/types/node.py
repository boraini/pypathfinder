from pathfinder.types.path import *
class Node():
    def __init__(self, name):
        self.name = name
        self.paths = []
        self.cost = 1e7
        self.before = None
    def __str__(self):
        out = ""
        for path in self.paths:
            out = out + str(path)
        return "Node " + self.name + " has paths to " + out
    def addPath(self, target, cost):
        self.paths.append(Path(target, cost))
