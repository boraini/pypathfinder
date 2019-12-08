class Path(object):
    def __init__(self, target, cost):
        self.target = target
        self.cost = cost
    def __str__(self):
        return self.target.name + " (" + str(self.cost) + "),"
