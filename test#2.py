#!/usr/bin/python

def reverse_names(names):
  
  for name in reversed(names):
    print ('Hello ' name ', nice to meet you.')
    
  return names    

def main():
   names = ["Diego", "Chase", "Xavier", "Sebastian", "Sean", "Paige", "Camila"]
   reverse_names(names)