#!/usr/bin/env python
import sys,os

lst=["a","b","c","d","e","f"]
lst[2:2]=["ab"]
print(lst)
lst[2:4]=["x"]
print (lst)
print (lst.pop())
print (lst)
lst.append("g")
print(lst)
for i in range(len(lst)):
    print(i)
    print(lst[i])
lst.sort()
print(lst)
lst.reverse()
print(lst)
m=["aa","a","c"]
lst.extend(m)
print (lst)
a=lst.count(1)
print (a)
