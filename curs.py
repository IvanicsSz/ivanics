import curses,time,random
from curses import wrapper

#initialize the screen, write a string and close
def write(stdscr):
    screen=curses.initscr()
    #curses.noecho()
    #curses.cbreak()
    curses.start_color()
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_YELLOW)
    color=1 #color number
    dims=[]
    dims=screen.getmaxyx()
    screen.clear()
    for i in range(dims[0]): #iterate the y axis
        for k in range(dims[1]-6): #iterate the x axis
            if (k%6==0 and random.randint(0,1)==1):#k to read hello random for place or not to place
                screen.addstr(i,k,"hello",curses.color_pair(color))#+str(dims) //color the string
                screen.refresh()
                time.sleep(0.02)
                color+=1
                if (color>2):
                    color=1
    screen.getch() #wait for press random key
    screen.endwin() #eitx from the screen

#run function without error, and to get the terminal in a right way
wrapper(write)
