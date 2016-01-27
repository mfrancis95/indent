from argparse import ArgumentParser
from re import sub
import sys

parser = ArgumentParser("reindent")
parser.add_argument("spaces", type = int)
parser.add_argument("to", type = int)
args = parser.parse_args()

regex = "^" + " " * args.spaces + r"\b"
substitute = " " * args.to

for line in map(lambda line: sub(regex, substitute, line), sys.stdin):
    sys.stdout.write(line)
