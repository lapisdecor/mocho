#!/usr/bin/env python3

def mdc(a,b):
...     while b:
...         a, b = b, a%b
...     return a
... 

mdc(10,15)
