from pathfinder.types.node import Node
import numpy, itertools
import png
import pathlib
class RasterReader(object):
    def __init__(self, nodes, readPath):
        self.neighbors = 4
        self.readPath = readPath
        self.path = "./raster.png"
        self.naming = "x,y"
        self.lowerThreshold = -1
        self.upperThreshold = 256
        self.channel = "r"
        self.nodes = nodes
        self.chandict = {
          "r": 0,
          "g": 0,
          "b": 0,
          "a": 0
        }
    def param(self, p):
        ls = p.split()
        print(ls)
        if (ls[0] == "neighbors"):
            self.neighbors = int(ls[1])
        if (ls[0] == "path"):
            self.path = ls[1]
        if (ls[0] == "naming"):
            self.naming = ls[1]
        if (ls[0] == "lowerThreshold"):
            self.lowerThreshold = int(ls[1])
        if (ls[0] == "upperThreshold"):
            self.upperThreshold = int(ls[1])
        if (ls[0] == "channel"):
            self.channel = self.chandict.get(ls[1], 0)
    def create(self):
        fullpath = str(pathlib.PurePath(self.readPath) / pathlib.PurePath(self.path))
        try:
            img = png.Reader(open(fullpath, "rb")).read()
        except:
            print("Error reading " +
            fullpath +
            "This graphdb implementation currently only supports PNG rasters.")
            return 1
        image_2d = img[2]
        image_2d = numpy.vstack(image_2d)
        gen = list()
        gen = [
            [{} for _ in range(int(len(image_2d[0]) / 4))] for _ in range(len(image_2d))
        ]
        print(len(gen), len(gen[0]))
        #for ix in range(int(len(gen) / 4)):
    #        gen[ix] =
        for y in range(0, len(image_2d)):
            for x in range(0, int(len(image_2d[0]) / 4)):
                if self.isEmpty(image_2d, x, y):
                    nd = Node(self.naming.replace("x", str(x)).replace("y", str(y)))
                    self.nodes.append(nd)
                    gen[y][x] = nd
        if self.neighbors == 8:
            self.connect8(gen)
        else:
            self.connect4(gen)
    def isEmpty(self, img, x, y):
      return (img[y][x * 4] > 127)
    def connect4(self, gen):
        for y in range(0, len(gen)):
            for x in range(0, len(gen[0])):
                if (gen[y][x]):
                    if x + 1 < len(gen[0]) and gen[y][x + 1]:
                        gen[y][x].addPath(gen[y][x + 1], 1)
                    if (x - 1 > 0) and (gen[y][x - 1]):
                        gen[y][x].addPath(gen[y][x - 1], 1)
                    if y + 1 < len(gen) and (gen[y + 1][x]):
                        gen[y][x].addPath(gen[y + 1][x], 1)
                    if (y - 1 > 0) and (gen[y - 1][x]):
                        gen[y][x].addPath(gen[y - 1][x], 1)
