"""
Field - extract fields from a file
Copyright (C) 2015 Trevor Bramwell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import sys
from argparse import ArgumentParser, FileType


parser = ArgumentParser(description='Extract fields from a file.')

parser.add_argument(
    '-f', '--file', dest='filename', metavar='FILE', default=sys.stdin,
    type=FileType('r'), help='the file where fields come from')

parser.add_argument(
    'columns', default=None, action='append',
    nargs='*', type=int)

parser.add_argument(
    '-d', '--delimiter', default=None,
    help='delimiter between fields', type=str)


def split_lines(filehandle, delim):
    for line in filehandle:
        yield line.strip('\n').split(delim)


def extract_fields(filehandle, delim, columns):
    lines = split_lines(filehandle, delim)
    for line in lines:
        if max(columns) <= len(line):
            yield (line[c-1] for c in columns)


def main():
    """
    Main Entry Point
    """
    args = parser.parse_args()
    filehandle = args.filename
    delim = args.delimiter
    columns = args.columns[0]

    if not columns:
        for line in filehandle:
            print line,
        exit(0)

    fields = extract_fields(filehandle, delim, columns)

    for line in fields:
        print ' '.join(line)

    args.filename.close()
