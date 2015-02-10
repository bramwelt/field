Name
====

    field - extract fields from files

SYNOPSIS
========

    ```bash
    field [-h] [-f FILE] [-d DELIMITER] [field [field ...]]
    ```

DESCRIPTION
===========

Field extracts a list of fields (columns) from a files. It is
a simpler version of `awk '{ print $1; }'`. Given no arguments, field
with simply output the file. Given fields


By default field reads from stdin and writes to stdout, using a field
delimiter of whitespace (\<space\>\<tab\>).

OPTIONS
=======

`-f FILE`, `--file FILE` - Extract fields from each line of the FILE.
To extract
fields from a file, the `-f` flag is provided.

To change how fields are identified, a delimiter between fields can be
set with `-d`. By default the delimiter is run of whitespace characters.

EXAMPLE
=======

AUTHOR
======
