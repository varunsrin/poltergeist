#!/usr/bin/python

import argparse
import os.path as path
from pydub import AudioSegment, pyaudioop

output_fmt = 'wav'

parser = argparse.ArgumentParser()
parser.add_argument("-i", action="store", dest="input_path")
parser.add_argument("-o", action="store", dest="output_path")
args = parser.parse_args()

if args.input_path == None:
  raise Exception("no source file provided with -i argument")

if args.output_path == None:
  input_root, input_ext = path.splitext(args.input_path)
  output_path = input_root + "." + output_fmt
else:
  output_path = args.output_path

try:
  source = AudioSegment.from_file(args.input_path)
  inverted =  source._spawn(data=pyaudioop.mul(source._data,
                                               source.sample_width,
                                               -1.0))
  inverted.export(output_path, format=output_fmt)

except IOError:
  print "Source file " + args.input_path + " could not be opened"
  print IOError
