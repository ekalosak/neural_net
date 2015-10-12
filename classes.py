import uuid
import itertools as itt
import random

class Node(object):

    def __init__(self, x = None, y = None):
        self.name = uuid.uuid4()
        if x and y:
            self.location = x, y
        elif x or y:
            raise Exception("Invalid location: gave x or y but not both")

class Edge(object):

    def __init__(self, n1, n2):
        assert all([type(n) == Node for n in [n1, n2]])
        self.nodes = [n1, n2]

class WeightEdge(Edge):

    def __init__(self, weight, n1, n2):
        Edge.__init__(self, n1, n2)
        self.weight = weight

class Graph(object):

    def __init__(self, edges = [], nodes = []):
        self.edges = edges
        self.nodes = nodes
        self.validate()

    def validate(self):
        assert all([type(e) == Edge for e in self.edges])
        assert all([type(n) == Node for n in self.nodes])
        assert all([all([a in self.nodes for a in b.nodes])
            for b in self.edges])

class Perceptron(Node):

    def __init__(self, inputs = [], weights = [], bias = 1):
        assert all([type(i) == Perceptron for i in inputs])
        assert all([type(w) == WeightEdge for w in weights])
        assert len(inputs) == len(weights)

        self.thresh = thresh
        self.inputs = inputs
        self.weights = weights

    def sigmoid(x):
        return 1 / (1 + math.exp(x))

def test():
    nv = 10
    ne = 40
    nds = [Node() for i in range(nv)]
    edgnds = random.sample([a for a in itt.product(nds, nds)], ne)
    edgs = [Edge(b, c) for b, c in edgnds]
    g = Graph(edges = edgs, nodes = nds)
    print "Passed tests!!"

if __name__ == "__main__":
    test()
