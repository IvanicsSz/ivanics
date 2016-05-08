#!/usr/bin/env python
print ("My first simple Python script!")
name = ("hello world")


for i in name:
    print (i)
    k=0
    for j in name:
        if i == j:
            k=k+1

    print (k)
