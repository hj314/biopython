# Copyright 2001 by Katharine Lindner.  All rights reserved.
# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.

#!/usr/bin/env python
"""Test the MetaTool parser and make sure everything is working smoothly.
"""
# standard library
import os
import copy
import sys

# Biopython
from Bio import File

from Bio import MetaTool

kabat_file_dir = os.path.join(os.getcwd(), 'MetaTool')

test_files = [ 'meta.out', 'meta9.out' ]



record_parser = MetaTool.RecordParser( )

for test in test_files:
    datafile = os.path.join( 'MetaTool', test )
    src_handle = open( datafile )
    iterator = MetaTool.Iterator(src_handle, record_parser)
    data = iterator.next()
    print data

