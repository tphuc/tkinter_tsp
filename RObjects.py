from mathDistance import EuclideanDistance, SumDistance


class Node:
    def __init__(self, name, y, x):
        self.name = name
        self.y = y
        self.x = x
        self.loc = (y, x)



class Graph:
    def __init__(self, Nodes):
        self.Nodes = Nodes

    def totalDistance(self):
        return SumDistance([node.loc for node in self.Nodes])
    def calFitness(self):
        return 1 / self.totalDistance()
    def displayRoute(self):
        for node in self.Nodes:
            print(node.name, end='->')
        print('')