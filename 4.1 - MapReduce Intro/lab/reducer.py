#!/usr/bin/env python

import sys

valuetotal = 0
pastkey = None

for line in sys.stdin:
    data = line.strip().split('\t')

    newkey, newvalue = data

    if pastkey is not None and pastkey != newkey:
        print('{}\t{}'.format(pastkey, valuetotal))

        valuetotal = 0

    pastkey = newkey
    valuetotal  += float(newvalue)

if pastkey is not  None:
    print('{}\t{}'.format(pastkey, valuetotal))
