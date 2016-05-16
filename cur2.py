import sys,io

to_do=[]
status=[]
def file():
    f=open("thing.txt","a+")
    f.write(", ".join(to_do))
    #for i in f.read():
    #    print(i)
    f.close()
    return

while True:
    thing=input("Add some thing: ")
    if (thing=="DONE"):
        file()
        break

    to_do.append(thing)
#print (", ".join(to_do))
for i in to_do:
    print (i)
