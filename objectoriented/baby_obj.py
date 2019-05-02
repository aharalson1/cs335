#!/usr/bin/python -tt

import urllib
import re
import sys

class BabyNames : 
    def __init__(self, year):
        self.year = year
    
    def retrieve_names(self, url):
        #create a method to retrieve the names
        self.names = names
        self.url = url
        #self names = result
        
    def print_names(self):
      print self.names
        #iterate through self.names and print list
        
def main():
    args = sys.argv[1:]
    if not args:
      print 'usage: [--summaryfile] URL'
      sys.exit(1)
      
    summary = False
    if args[0] == '--summaryfile':
      summary = True
      del args[0]
      
    try:
        text = urllib.urlopen(args[0])
        if text.info().gettype() == 'text/html':
            years = re.findall(r'\d+\sto\s\d+</h2><ul>(.*?)</ul>', text.read())
            for year in years:
                #extract URl from the <li> tag and add URL to list
        #intantiating objects for getting baby names
        # we iteratie through the list of URLs from above
            for yearURL in yearURLs:
                bn = BabyNames(yearURL)
                bn.printNames()
       
    except IOError:
            print "Could not access web address "

if __name__ == '__main__':
  main()