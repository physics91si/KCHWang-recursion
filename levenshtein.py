#!/usr/bin/env python3

# Lab 16: Recursion
# Levenshtein Distance


def lev(a, b):
    if not a: # base case
        return len(b)
    elif not b:
        return len(a)
    else: # recursive case
        if a[-1] == b[-1]:
            return lev(a[0:-1], b[0:-1])
        else:
            dis1 = lev(a[0:-1], b[0:-1])
            dis2 = min(lev(a, b[0:-1]), lev(a[0:-1], b))
            return min(dis1, dis2) + 1
        





a = "armchair"
b = "armhair"
print ('test1: lev(%s, %s) = %d' % (a, b, lev(a, b)))

a = "physics"
b = "psychics"
print ('test2: lev(%s, %s) = %d' % (a, b, lev(a, b)))