#!/usr/bin/python -tt

for i in [11,9,7,2,0]:
    try:
        print "Number is: %d" % (100/i)
    except ZeroDivisionError:
        print "You can't divide by zero!"
        
        
