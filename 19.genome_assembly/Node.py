class Node:
    """ Class Node to represent a vertex in the de bruijn graph """
    def __init__(self, lab):
        self.label = lab
        self.indegree = 0
        self.outdegree = 0