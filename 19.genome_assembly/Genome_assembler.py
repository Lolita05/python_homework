#import argparse
import sys

class Node:
    """ Class Node to represent a vertex in the de bruijn graph """
    def __init__(self, lab):
        self.label = lab
        self.indegree = 0
        self.outdegree = 0

class Edge:
    def __init__(self, lab):
        self.label = lab

def read_reads(input):
    """ Read short reads in FASTA format. One line in the input file correspond to one read. """
    f = open(input, 'r')
    lines = f.readlines()
    f.close()
    reads = []

    for line in lines:
        if line[0] != '>':
            reads = reads + [line.rstrip()]

    return reads

def construct_graph(reads, k=5):
    """ Construct de bruijn graph from sets of short reads with k length word"""
    edges = dict()
    vertices = dict()

    for read in reads:
        i = 0
        while i+k < len(read):
            v1 = read[i:i+k]
            v2 = read[i+1:i+k+1]
            if v1 in edges.keys():
                vertices[v1].outdegree += 1
                edges[v1] += [Edge(v2)]
            else:
                vertices[v1] = Node(v1)
                vertices[v1].outdegree += 1
                edges[v1] = [Edge(v2)]
            if v2 in edges.keys():
                vertices[v2].indegree += 1
            else:
                vertices[v2] = Node(v2)
                vertices[v2].indegree += 1
                edges[v2] = []
            i += 1

    return (vertices, edges)

def output_contigs(g):
    """ Perform searching for Eulerian path in the graph to output genome assembly"""
    V = g[0]
    E = g[1]
    # Pick starting node (the vertex with zero in degree)
    start = list(V.keys())[0]
    for k in V.keys():
        if V[k].indegree < V[start].indegree:
            start = k
    contig = start
    current = start
    while len(E[current]) > 0:
        # Pick the next node to be traversed (for now, at random)
        next = E[current][0]
        del E[current][0]
        contig += next.label[-1]
        current = next.label
    return contig

def assembly(input_file, k=5, output_file):
    reads = read_reads(input_file)
    g = construct_graph(reads, k)
    contig = output_contigs(g)
    with open(output_file, 'w') as output:
        output.write(f">output_contig\n{contig}\n")


#if __name__ == "__main__":
    #parser = argparse.ArgumentParser(prog='debruijn_genome_assembler', description='De Brujin genome assembler tool')
    #parser.add_argument('-i', '--input_file', required=True, type=str, help='fasta file with short reads')
    #parser.add_argument('-k', default=5, type=int, help='k-mers length')
    #parser.add_argument('-o', '--output_file', type=str, help='fasta file with whole contig')
    #args = parser.parse_args()
    #assembly(args['input_file'], args['k'], args['output_file'])
