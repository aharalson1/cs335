#!/usr/bin/env python3

import sys

def mult(x,y):
    print (str(x*y))

if __name__ == '__main__' :
  a = int(sys.argv[1])
  b = int(sys.argv[2])
  mult(a,b)
    