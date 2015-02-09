#! /usr/bin/env python
"""
Field

Written by Trevor Bramwell

License: GPLv2
"""
import sys
from argparse import ArgumentParser, FileType


parser = ArgumentParser(description='Extract fields from a stream.')

parser.add_argument(
    '-f', '--file', dest='filename', metavar='FILE', default=sys.stdin,
    type=FileType('r'), help='the file where fields come from')

parser.add_argument(
        'columns', default=None, action='append',
        nargs='*', type=int)

parser.add_argument(
        '-d', '--delimiter', default=None,
        help='delimiter between fields', type=str)


args = parser.parse_args()
filehandle = args.filename
delim = args.delimiter
columns = args.columns[0]

if not columns:
    for line in filehandle:
        print line,
    exit(0)

lines = (line.strip('\n').split(delim) for line in filehandle)
fields = ((line[c-1] for c in columns) for line in lines if max(columns) <= len(line))

for line in fields:
    print ' '.join(line)
        
args.filename.close()
