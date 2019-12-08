from pathfinder.types.node import Node
import png
class RasterReader(object):
    def __init__(self, nodes, readPath):
        self.neighbors = 4
        self.readPath = readPath
        self.path = "raster.png"
        self.naming = "x,y"
        self.lowerThreshold = -1
        self.upperThreshold = 256
        self.channel = "r"
    def param(self, p):
        ls = p.split()
        if (p[0] == "neighbors"):
            self.neighbors = int(p[1])
        if (p[0] == "path"):
            self.path = p[1]
        if (p[0] == "naming"):
            self.naming = p[1]
        if (p[0] == "lowerThreshold"):
            self.lowerThreshold = int(p[1])
        if (p[0] == "upperThreshold"):
            self.upperThreshold = int(p[1])
        if (p[0] == "channel"):
            self.channel = p[1]
    def create(self):
        fullpath = pathlib.PurePath(self.readPath) / pathlib.PurePath(self.path)
        try:
            pypng.open(fullpath)
        except:
            print("Error reading " +
            fullpath +
            "This graphdb implementation currently only supports PNG rasters.")
            return 1
