#!/usr/bin/env python

import sys

print ("Finonacci first 30 sequence")
sequence=input("enter the sequence:")
#fac=factorial(sequence)
i=1
f=1
while (i<int(sequence)):
    if (i==1):
        f=f
    else:
        f+=f
    i+=1
    print ("%i. %i" %(i,f))
