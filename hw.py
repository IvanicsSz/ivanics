#!/usr/bin/env python

import sys

def main(argv):
    argLen=len(sys.argv)
    if (argLen==1):
        print("Hello World")
    elif(argLen>1):
        i=0
        while (i+1<argLen):
            print ("Hello "+sys.argv[i+1]+"!")
            i+=1
if __name__ == "__main__":
   main(sys.argv[1:])
