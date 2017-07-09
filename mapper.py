#!/usr/local/bin/python
import sys
input = sys.stdin
for line in input:
    line = line.strip()
    words = line.split()
    for word in words:
        print "{}\t{}".format(word, 1)
