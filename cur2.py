import sys,io

to_do=[]
status=[]

def show_help():
    print("""key worlds:
    DONE: to exit
    SHOW: to check list
    HELP: for this help
    """)
def file():
    f=open("thing.txt","a+")
    f.write(", ".join(to_do))
    #for i in f.read():
    #    print(i)
    f.close()

def write_list():
    to_do.append(thing)
    print ("added {} to your list, list's lenght{}".format(thing,len(to_do)))

def show_list():
    for i in to_do:
        print (i)

show_help()
while True:
    thing=input("Add some thing: ")
    if (thing=="DONE"):
        file()
        break
    elif (thing=="HELP"):
        show_help()
        continue
    elif (thing=="SHOW"):
        show_list()
        continue

    write_list()

show_list()
#print (", ".join(to_do))
