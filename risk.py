#!/usr/bin/env python

import sys
import random
import functools

def rndNumber():
    return random.randrange(1,7)

attack=[rndNumber(),rndNumber(),rndNumber()]
defender=[rndNumber(),rndNumber()]
#sorted(attack,key=functools.cmp_to_key(reverse_numeric))
#sorted(defender,key=functools.cmp_to_key(reverse_numeric))
attack=sorted(attack,reverse=True)
defender=sorted(defender,reverse=True)

print (attack,defender)
if (max(attack)>max(defender)):
    print ("attacker has win")
else:
    print ("defender wins")
