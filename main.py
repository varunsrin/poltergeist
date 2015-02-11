#!/usr/bin/python

import sys

path = ''
if sys.argv[1] == "-i":
  path = sys.argv[2]
  print "Source: " + path
else:
  raise Exception("no source file provided in the format main.py -i <path to file>")
