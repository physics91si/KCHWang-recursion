#!/usr/bin/env python3

# Lab 16: recursion
# Fibonacci with cache

cache = {} # n => fib(n)

def fib(n):
    # base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        fib_sum = fib(n - 1) + fib(n - 2)
        cache[n] = fib_sum
        return fib_sum
    
    

print("fib(40):", fib(40))
