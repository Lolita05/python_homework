import argparse
import logging
from Node import Node
from Edge import Edge

logging.basicConfig(filename='app_photo_filter.log', filemode='w', format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug('reading reads')
def read_reads(input_file):
    """ Read short reads in FASTA format. One line in the input file correspond to one read. """
    f = open(input_file, 'r')
    lines = f.readlines()
    f.close()
    reads = []

    for line in lines:
        if line[0] != '>':
            reads = reads + [line.rstrip()]

    return reads

logger.debug('constructing graph')
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
    logger.debug('creating contig')
    return contig

def assembly(input_file, k, output_file):
    reads = read_reads(input_file)
    g = construct_graph(reads, k)
    contig = output_contigs(g)
    with open(output_file, 'w') as output:
        output.write(f">output_contig\n{contig}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='debruijn_genome_assembler', description='De Brujin genome assembler tool')
    parser.add_argument('-i', '--input_file', required=True, dest='input_file')
    parser.add_argument('-k', default=5, type=int)
    parser.add_argument('-o', '--output_file', default = 'out.fasta', dest='output_file')
    args = parser.parse_args()
    assembly(input_file = args.input_file, k = args.k, output_file = args.output_file)
