#! /bin/bash

groff -Tascii -man field.1.man | gzip > field.1.gz
