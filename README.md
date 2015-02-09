Field
=====

```
field [-h] [-f FILE] [-d DELIMITER] [field [field ...]]

Extract fields from a stream.

optional arguments:
  -f FILE, --file FILE  The file where fields come from
  -d DELIMITER, --delimiter DELIMITER Delimiter between fields
```

Field is a program from extracting fields (columns) from a stream. It is
a simpler version of `awk '{ print $1; }'`

By default field reads from stdin and writes to stdout. To extract
fields from a file, the `-f` flag is provided.

To change how fields are identified, a delimiter between fields can be
set with `-d`. By default the delimiter is run of whitespace characters.
