"""
Pick the corpus to load at the command line by supplying the --corpus flag.
"""
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--corpus', action='store', dest='corpus')
CORPUS = parser.parse_args().corpus

def main():
   if CORPUS == 'bbcnews':
      from bbcnews import data, target
      print(len(data), len(target))
   elif CORPUS == 'newsgrp':
      from newsgrp import data, target
      print(len(data), len(target))
   else:
      raise Exception("Corpus not found.")

if __name__ == "__main__":
   main()