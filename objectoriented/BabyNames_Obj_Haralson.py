#BabyNames Object-Oriented Program
# Ashton Haralson

#!/usr/bin/python -tt

# Web address: https://www.babycentre.co.uk/popular-baby-names

import urllib
import re
import sys

class Babynames :
    year = None
    gender = ''
    names = {}
    
    def __init__(self, url):
        self.url = url
        
    def build_names(self):
        # Grab year
        self.year = self.url[-4:]
        
        # Grab male gender
        if bool(re.search(r'boy', self.url)):
            self.gender = 'Boy'
        
        # Grab female gender    
        elif bool(re.search(r'girl', self.url)):
            self.gender = 'Girl'
        
        # Create names
        pagetext = urllib.urlopen(self.url).read()
        
        ol_lists = re.findall(r'<ol.*?/ol>', pagetext, re.DOTALL)
        
        # Grabs names from url
        if len(ol_lists) != 0:
            
            i = 1
            for list in ol_lists:
                matches = re.findall(r'<a.*?>(\w*?)</a>', list, re.DOTALL)
                
                if len(matches) == 0:
                    matches = re.findall(r'<li> (\w*?) </li>', list)
                
                for match in matches:
                    self.names[i] = match
                    i += 1
                
        else:
            i = 1
            matches = re.findall(r'<a href="[\w/]*?">(\w*?)</a>', pagetext, re.DOTALL)
            
            for match in matches:
                self.names[i] = match
                i += 1
        
        
    def output(self, file):
        
        # Open output file
        f = open(file, 'w')
        
        if len(self.gender) > 0:
            f.write('Popular ' + self.gender + ' Baby Names in ' + self.year)
        else:
            f.write('Popular Baby Names in ' + self.year)
            
        f.write('\n' + '-----------------------------' + '\n')
        
        for item in self.names.keys():
            f.write( str(item) + ". " + self.names[item] + '\n')
    
def main():
    
    args = sys.argv[1:]
    
    if not args:
        print 'usage: [--summaryfile] URL'
        sys.exit(1)
    
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
    
    if summary:
        
        # Trys to open URL
        try:
            text = urllib.urlopen(args[1])
            
            if text.info().gettype() == 'text/html':
                
                link_lists = re.findall(r'\d+\sto\s\d+</h2><ul>(.*?)</ul>', text.read())
                
                root_url = re.search(r'https://([\w.]*)', args[0])
                babynames_list = []
             
                for item in link_lists:
                    links = re.findall(r'<a href="(.*?)">', item)
                
                    # BabyNames object
                    for link in links:
                        babynames_list.append( Babynames(root_url.group() + link) )
                    
                # Send to file
                for item in babynames_list:
                    item.build_names()
                    item.output(item.gender + 'babynames' + item.year + '.txt')
                
        except IOError:
            print "could not access web address"
            
    else:
        print 'unrecognized command \'', args[0], '\''
        sys.exit(1)
        
        
        
if __name__ == '__main__':
    main()