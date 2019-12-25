import numpy #pip3 install numpy
from pathfinding.core.grid import Grid #pip3 install pathfinding
from pathfinding.finder import a_star, best_first, bi_a_star, breadth_first, dijkstra
from timeit import timeit #pip3 install timeit
import png #pip3 install pypng

#Have a file named maze.png in exec directory.
try:
    img = png.Reader(open("rm2020.png", "rb")).read()
except:
    print("Error reading")
image_2d = img[2]
image_2d = numpy.vstack(list(image_2d))
gen = list()
gen = [
    [0 for _ in range(int(len(image_2d[0]) / 4))] for _ in range(len(image_2d))
]
for y in range(len(gen)):
    for x in range(len(gen[0])):
        gen[y][x] = 1 if image_2d[y][x * 4] > 127 else 0

matrix = gen

#for _ in matrix:
#    print(_)

grid = Grid(matrix=matrix)

start = grid.node(24, 3)
goal = grid.node(24, 26)

finderlist = [
    ("A*", a_star.AStarFinder()),
    ("Bidirectional A*", bi_a_star.BiAStarFinder()),
    ("Breadth First Search", breadth_first.BreadthFirstFinder()),
    ("BFS", best_first.BestFirst()),
    ("Dijkstra's", dijkstra.DijkstraFinder()),
#    ("Iterative-Deepening A*", ida_star.IDAStarFinder())
]

def finderGenerator():
    i = 0
    while i < len(finderlist):
        yield finderlist[i]
        i += 1

gen = finderGenerator()

(finderName, finder) = next(gen)

def finderTestFunc():
    grid.cleanup()
    return finder.find_path(start, goal, grid)

while finder:
    time = timeit(finderTestFunc, number=int(1e2)) * 1e-2
    path, runs = finderTestFunc()
    print('Algorithm: ', finderName)
    print('time:', time, ' operations:', runs, ' path length:', len(path))
    print(grid.grid_str(path=path, start=start, end=goal))
    print('\n'*5)
    (finderName, finder) = next(gen)
