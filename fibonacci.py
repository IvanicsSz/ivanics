#!/usr/bin/env python

import sys

print ("Finonacci first 30 sequence")
i=1
f=1
while (i<31):
    if (i==1):
        f=f
    else:
        f+=f
    i+=1
    print ("%i. %i" %(i,f))
