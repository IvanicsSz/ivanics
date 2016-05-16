import sys,io

to_do=[]
status=[]
def quit():
    print (", ".join(to_do))
    exit()
def file():
    f=open("thing.txt","a")
    f.write(", ".join(to_do))
    f.close()
    return

while True:
    thing=input("Add some thing: ")
    if (thing=="DONE"):
        file()
        quit()
    else:
        to_do.append(thing)
