from pathfinder.types.node import Node
from pathfinder.extensions.rasterreader import RasterReader
from os import path as ospath
class Graph(object):
    """Graph Data"""
    def __init__(self, file):
        self.nodes = []
        self.name = ""
        f = open(file, "+r")
        f1 = f.readlines()
        mode = "NAME"
        ext = None
        for cmd1 in f1:
            if cmd1.isspace():
                continue
            cmd = cmd1.strip()
            if cmd == "NODES":
                mode = "NODES"
                continue
            if cmd == "PATHS":
                mode = "PATHS"
                continue
            if cmd == "RASTER":
                mode = "EXT"
                ext = RasterReader(self.nodes, ospath.dirname(f.name))
                continue
            if cmd == "END":
                mode = "COMMENT"
                ext.create()
                continue
            if cmd == "COMMENT":
                mode = "COMMENT"
                continue
            if mode == "NAME":
                self.name = cmd
                continue
            if mode == "NODES":
                ls = cmd.split() #may add further words such as spatial coordinates
                self.nodes.append(Node(ls[0]))
                if (ls[2]):
                    self.nodes[-1].x = float(ls[1])
                    self.nodes[-1].y = float(ls[2])
                continue
            if mode == "PATHS":
                ls = cmd.split()
                a = None
                b = None
                for node in self.nodes:
                    if node.name == ls[0]:
                        a = node
                    if node.name == ls[1]:
                        b = node
                if a and b:
                    a.addPath(b, float(ls[2]))
                    b.addPath(a, float(ls[2]))
            if mode == "EXT":
                ext.param(cmd)
        f.close()
    def __str__(self):
        out = ""
        for node in self.nodes:
            out = out + "\n" + str(node)

        return "Graph: " + self.name + out
    def get(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
    def clear(self):
        for node in self.nodes:
            node.clear()
