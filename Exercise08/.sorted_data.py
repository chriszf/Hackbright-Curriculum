#!/bin/env python

f = open("scores.txt")
scores = {}
for line in f:
    k,v = line.split(":")
    scores[k] = int(v)

sorted_keys = scores.keys()
sorted_keys.sort()

for key in sorted_keys:
    print "Restaurant %r is rated at %d."%(key, scores[key])
