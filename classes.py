import uuid
import itertools as itt
import random

''' NOTES
1. there could be duplicate edges
2. might think about implementing n1 -> n2 as directed?
'''

class Node(object):

    def __init__(self, x = None, y = None):
        self.name = uuid.uuid4()
        if x and y:
            self.location = x, y
        elif x or y:
            raise Exception("Invalid location: gave x or y but not both")

class Edge(object):

    def __init__(self, n1, n2):
        self.nodes = [n1, n2]
        self.validate()

    def validate(self):
        assert self.nodes[0] != self.nodes[1]
        assert all([type(n) == Node for n in [n1, n2]])
        assert len(self.nodes) == 2

class WeightEdge(Edge):

    def __init__(self, n1, n2, weight = 1):
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

    def __init__(self, inputs = [], wedges = [], bias = 1):
        assert all([type(i) == Perceptron for i in inputs])
        assert all([type(w) == WeightEdge for w in wedges])
        assert len(inputs) == len(wedges)

        self.thresh = thresh
        self.inputs = inputs
        self.wedges = wedges

        self.validate()

    def sigmoid(x):
        return 1 / (1 + math.exp(x))

    def feed_forward(self):
        k = self.bias
        for i in self.wedges:
            if i[0] == self:
                k = k + i[1] * i.weight
            elif i[1] == self:
                k = k + i[0] * i.weight
        return sigmoid(k)

    def validate(self):
        for w in self.wedges:
            assert w[0] == self or w[1] == self
            assert not w[0] == w[1]
            assert isinstance(w.weight, (int, long, float))

class Neural_Net(Graph):

    def __init__(self, perceptrons = []):
        self.perceptrons = perceptrons
        self.wedges = []
        for p in self.perceptrons:
            for w in p.wedges:
                self.wedges.append(w)

        self.validate()

    def validate(self):
        for p in self.perceptrons:
            assert type(p) == Perceptron
        for w in self.wedges:
            assert type(w) == WeightEdge

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
