#!/usr/local/bin/python
import sys
input = sys.stdin
current_count = 0
current_word = None
for line in input:
    line = line.strip()
    key, value = line.split("\t")
    value = int(value)
    if key == current_word:
        current_count += value
    else:
        if current_word:
            print "{}\t{}".format(current_word, current_count)
            current_count = value
            current_word = key
        else:
            current_word = key
            current_count = value
print "{}\t{}".format(current_word, current_count)
