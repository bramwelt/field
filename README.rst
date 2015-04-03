Name
====

**field** - extract fields from a file

SYNOPSIS
--------

.. code:: bash

    field [-h] [-f FILE] [-d DELIMITER] [FIELD ...]

DESCRIPTION
-----------

**field** extracts a list of fields from a file. It is a simpler
version of::

    awk '{ print $5,$3,$1; }'

and similar scripts. Whitespace delimited (space and  tab)  fields  are
read from stdin and written to stdout.

FIELD  is  assumed  to be 1-indexed integer, separated by commas and/or
spaces, and take the following form:

      N      a single field.

      N-M    a range of increasing or decreasing fields from N to M.

**-h**, **--help**
      show concise list of options and exit

**--version**
      display version information and exit

**-f**, **--file** *FILE*
      an explicit file to extract fields

**-d**, **--delimiter** *DELIMITER*
      character delimiter between fields

NOTES
-----

Field was written to address two short comings of cut:

1. Default Behavior

   The default delimiter of cut is tab. Most command line utilities
   produce  output  delimited by whitespace, which includes spaces.
   Field takes this into account and defaults the delimiter to both
   tab and space characters.

2. Field Ordering

   Fields  extracted  by  cut  are not listed in the order they are
   passed.

EXAMPLES
--------

.. code:: bash

    $ mount | field 5 3 1
    ext4 / /dev/mapper/sda7_crypt
    proc /proc proc
    sysfs /sys sysfs

.. code:: bash

    $ ls -l /usr/local/bin/ | field 1 9
    -rwxr-xr-x airbrake*
    -rwxr-xr-x bayes.rb*
    -rwxr-xr-x bourbon*

.. code:: bash

    $ cat /etc/mtab | cut -d' ' -f 4 | field -d',' 1 4 3 2
    rw gid=5 nosuid noexec
    rw size=10% nosuid noexec
    rw nodev nosuid noexec
    rw user=root nodev nosuid

AUTHOR
------

Written by Trevor Bramwell.

COPYRIGHT
---------

Copyright (C) 2015 Trevor Bramwell License GPLv3+: GNU GPL version 3 or
later <http://gnu.org/licenses/gpl.html>.
This  is  free  software:  you  are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
