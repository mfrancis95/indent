from argparse import ArgumentParser
from re import sub
import sys

parser = ArgumentParser("reindent")
parser.add_argument("-f", "--file")
parser.add_argument("spaces", type = int)
parser.add_argument("to", type = int)
args = parser.parse_args()

regex = "^(" + " " * args.spaces + r")(?=\S)"
substitute = " " * args.to

def reindent(file):
    for line in map(lambda line: sub(regex, substitute, line), file):
        sys.stdout.write(line)

file = args.file
if file:
    with open(file) as f:
        reindent(f)
else:
    reindent(sys.stdin)
