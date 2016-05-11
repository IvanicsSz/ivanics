#!/usr/bin/env python
import sys

#print ("What is your new idea?")
idea=input("What is your new idea?")
handle=open("handle.txt","wb")
handle.write(bytes(idea,'UTF-8'))
handle.close()
