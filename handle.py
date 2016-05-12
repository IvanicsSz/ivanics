#!/usr/bin/env python
import sys

#print ("What is your new idea?")
idea=input("What is your new idea?")
#idea="New idea"
handle=open("handle.txt","wb")

store={"0.":""}
store1=store.update({str(len(store))+'. ':idea})
handle.write(bytes(str(store)+"/n",'UTF-8'))
handle.close()

for i,k in enumerate(store):
    print (k,i)
