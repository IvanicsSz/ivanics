#!/usr/bin/env python

import sys

def main(argv):
    argLen=len(sys.argv)
    if (argLen==1):
        print("Hello World")
    elif(argLen>1):
        print ("Hello "+sys.argv[1]+"!")

if __name__ == "__main__":
   main(sys.argv[1:])
