Name
====

field - extract fields from a file

SYNOPSIS
========

.. code:: bash

    field [-h] [-f FILE] [-d DELIMITER] [field [field ...]]

DESCRIPTION
===========

Field extracts a list of fields or columns from a file. It is a simpler
version of ``awk '{ print $1; }'``.

Default is to read whitespace (\<space\>\<tab\>) delimited text from
_stdin_ and write fields to _stdout_.

OPTIONS
=======

- ``-f FILE``, ``--file FILE`` - Extract fields from each line of the _FILE_.
  Defaults to _stdin_.

- ``-d DELIMITER``, ``--delimiter DELIMITER`` - Single character used to
  distinguish between fields. Defaults to whitespace (\<space\>\<tab\>).


EXAMPLE
=======

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

    cat /etc/mtab | cut -d' ' -f 4 | field -d',' 1 4 3 2
    rw gid=5 nosuid noexec
    rw size=10% nosuid noexec
    rw nodev nosuid noexec
    rw user=root nodev nosuid

AUTHOR
======

Written by Trevor Bramwell.

COPYRIGHT
=========

Copyright © 2015 Trevor Bramwell. License GPLv3+: GNU GPL version 3 or later
<http://gnu.org/licenses/gpl.html>.  This is free software: you are free
to change and redistribute it.  There is NO WARRANTY, to the extent
permitted by law.
