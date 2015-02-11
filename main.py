#!/usr/bin/python

import sys
from pydub import AudioSegment

path = ''
if sys.argv[1] == "-i":
  path = sys.argv[2]
else:
  raise Exception("no source file provided in the format main.py -i <path to file>")

destination = path + ".mp3"

try:
  AudioSegment.from_file(path).export(destination, format='mp3')
except IOError:
  print "Source file " + path + " not found"
  print IOError

