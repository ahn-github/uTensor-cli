import argparse
import os
import shutil
import sys
from view_node import GraphInspector, load_graph

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-q", "--quantize", help="Quantize graph", action="store_true")
parser.add_argument("-o", help="override output name", metavar="NAME")
parser.add_argument("file", help="input protobuf file")

def process_graph(fName):
    graph = load_graph(fName, name="")
    inspector = GraphInspector(graph)
    bName = os.path.splitext(os.path.basename(fName))[0]

    # Handle optional quantization

    # Dump the constants to IDX files
    if os.path.exists(bName):
        shutil.rmtree(bName)
    os.mkdir(bName)

    for i in graph.get_operations():
        if i.type == "Const":
            inspector.snap(i.name, path=bName)



def main():
    args = parser.parse_args()
    if args.verbose:
        print "verbosity turned on"

    process_graph(args.file)

if __name__ == '__main__':
    main()
