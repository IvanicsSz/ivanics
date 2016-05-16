import time, random
import sys

#generate a random number between 1,10

#get a number gess from the player

def main():
    secret=random.randint(1,10)
    players=[]
    cicle=0
    while len(players)<5:
        try:
            player=int(input("Guess one number: " ))

        except ValueError:
            print ("only integer!")

        #compare guess the secret number
        if player>secret:
            players.append(player)
            print ("Your number {} is bigger then the hidden".format(player))
        elif player<secret:
            players.append(player)
            print ("Your number {} is lower then the hidden".format(player))
        else:
            print ("Bingo the number is {}".format(secret))
            retry=input("TRY again? (Y or N): ")
            if retry=="Y":
                return main()
            else: break
    else:
            print("you did not gess")
            retry=input("TRY again? (Y or N): ")
            if retry=="Y":
                return main()
            else: exit()
main()
#print hit/miss
