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
from itertools import chain


parser = ArgumentParser(description='Extract fields from a file.')

parser.add_argument(
    '-f', '--file', dest='filename', metavar='FILE', default=sys.stdin,
    type=FileType('r'), help='the file where fields come from')

def column_converter(string):
    """
    Converts column arguments to integers.

    - Accepts columns in form of INT, or the range INT-INT.
    - Returns a list of one or more integers.
    """
    column = string.strip(',')
    if '-' in column:
        column_range = map(int, column.split('-'))
        # For decreasing ranges, increment the larger value, reverse the
        # passing to range (so it will accept the input), and finally
        # reverse the output ([::-1])
        if column_range[0] > column_range[1]:
            column_range[0] += 1
            return [i for i in range(*column_range[::-1])][::-1]
        # For normal ranges, increment the larger value.
        column_range[1] += 1
        return [i for i in range(*column_range)]
    if ',' in column:
        columns = column.split(',')
        return map(int, columns)
    return [int(column)]

parser.add_argument(
    'columns', default=None, action='append',
    nargs='*', type=column_converter)

parser.add_argument(
    '-d', '--delimiter', default=None,
    help='delimiter between fields', type=str)


def split_line(lines, delim):
    yield lines.strip('\n').split(delim)


def extract_fields(lines, delim, columns):
    for line in split_line(lines, delim):
        for c in columns:
            if check_columns(c, line, columns):
                yield line[c-1]

def check_columns(column, line, columns):
    """
    Make sure the column is the minimum between the largest column asked
    for and the max column available in the line.
    """
    return column <= min(len(line), max(columns))

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

    cs = list(chain.from_iterable(columns))
    fields = (extract_fields(line, delim, cs) for line in filehandle)

    for line in fields:
        print ' '.join(line)

    args.filename.close()
