import sys,io
import collections

a,b = (1,2)
tup=()
name="hello world"
for i in name:
    name=tuple(name)
    tup=name.count(i)
    print (tup)
print(a,b)
