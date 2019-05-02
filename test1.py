#!/usr/bin/python

import sys, math, csv

def extract_country(filename):
  
  
  f = open('http://una.dbms.rocks/assets/python/nuclear-plants.csv')
  csv_f = csv.reader(f)

  for row in csv_f:
    print row


if __name__ == '__main__':
  main()
