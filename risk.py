#!/usr/bin/env python

import sys
import random
import functools

def rndNumber():
    return random.randrange(1,7)
amult=input("attacker dice number:")
dmult=input("defender dice number")
#amult=7
#dmult=7
attack=[rndNumber()]
defender=[rndNumber()]

for i in range(0,int(amult)-1):

    attack.insert(i,rndNumber())

for k in range(0,int(dmult)-1):

    defender.insert(k,rndNumber())


attack=sorted(attack,reverse=True)
defender=sorted(defender,reverse=True)

print (attack,defender)
a=0
d=0
if (len(attack)>len(defender)):
    ln=defender

else:
    ln=attack


for i in range(len(ln)):
    if attack[i]>defender[i]:
        d+=1
    elif attack[i]<defender[i]:
        a+=1
    else:
        a=a
        d=d


print("attacker lose %i defender lose %i"%(a,d))
