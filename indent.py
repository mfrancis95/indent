from argparse import ArgumentParser
import indenter
import sys

parser = ArgumentParser("reindent")
parser.add_argument("-f", "--file")
parser.add_argument("spaces", type = int)
parser.add_argument("to", type = int)
args = parser.parse_args()

def indent(file):
    for line in indenter.indent(file, args.spaces, args.to):
        sys.stdout.write(line)

file = args.file
if file:
    with open(file) as f:
        indent(f)
else:
    indent(sys.stdin)
