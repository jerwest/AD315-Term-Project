import time
import random
from GameIntro import GameIntro
from Stats import Stats
from Chasm import Chasm
from Monsters import Monsters

items = ["a sword","chainmail","rope","gold"]
monsters = ["an ogre"]
stats = []
treasure = []
rooms = [
    {"north":1, "description":"The Chasm - Start Room #1"},
    {"south":0, "west":2, "description":"Room #2","items":[0]},
    {"east":1, "north":3, "description":"Room #3","items":[1]},
    {"south":2, "east":4, "description":"Room #4"},
    {"west":3, "north":5, "description":"Room #5"},
    {"south":4,"description":"Room #6","items":[2]},
]
 
def main():
    print("")
    current_room = 0 
    inventory = []
    
    GameIntro.screenWarning()
    GameIntro.gameTitle()
    stats = Chasm.chasmStart()

    time.sleep(1)
    print("\nThe earth beneath your feet begins to shake as bits of dirt crumble down the sides of the")
    print("chasm around you and then, before you, on the chasm wall, a door appears.")
    time.sleep(4)
    print("\n'You must type 'north' to enter the door, that is the only way to escape.' says the Voice.")
    time.sleep(3)
    accept = input("\nDo you accept? 'Yes' or 'No'? ").lower()
    time.sleep(1)
    while 1 == 1:
        if accept == "yes":
            break
        elif accept == "no":
            time.sleep(1)
            oldStats = stats
            stats = Stats.minusHealth(stats, 1)
            print("\nBurning pain comes from your left wrist again.")
            time.sleep(2)
            print("\nYou look at your forearm and see your HP go from", oldStats[0], "to", stats[0], ".")
            time.sleep(2)
            print("\nHelpless, you nod your head and agree to accept.")
            break
        else:
            time.sleep(2)
            accept = input("\nMust type either, 'Yes' or 'No'. ").lower()
    time.sleep(1)
    print("\n'Now go forth and attempt your escape from The Chasm', commands the Voice.")
    time.sleep(2)
    print(stats)

    
    while True:
        print()
        print(rooms[current_room]["description"] + "\n")

        #user action loop
        while True: 
     
            userInput = input("> ").lower()
     
            if userInput == "quit":
                exit()
     
            # movement
            if userInput in "northsoutheastwest":
                new_room = move_room(userInput, current_room)
                if new_room == -1:
                    print("You cannot move that way\n")
                else:
                    current_room = new_room
                    if current_room == "Room #2":
                        print("test room2")
                    break
                
            # search room
            if userInput == "search":
                search(current_room)

            # pick-up something
            if userInput == "pick-up":
                addItem = transfer(from_ = rooms[current_room]["items"],
                          to_ = inventory,
                          prompt="Pick up what?",
                          error="Nothing to pick up")
                print(addItem)
                if addItem == "a sword":
                    stats = Stats.addStrength(stats, 3)
                    print("Strength now: ", stats[1])
                elif addItem == "chainmail":
                    stats = Stats.addHealth(stats, 3)
                    print("Health now: ", stats[0])                    

            # drop something
            if userInput == "drop":
                minusItem = transfer(to_ = rooms[current_room]["items"],
                          from_ = inventory,
                          prompt="Drop what?",
                          error="Nothing to drop")
                if minusItem == "0":
                    stats = Stats.minusStrength(stats, 3)
                    print("Strength now: ", stats[1])

            #inventory
            if userInput == "inventory":
                show_inventory(inventory)

            #inventory
            if userInput == "stats":
                print(stats)

def move_room(inst, room):
    if inst in rooms[room]:
        return rooms[room][inst]
    else:
        return -1  
 
def search(room):
    print("\nThere is ", end = "")
    for m in rooms[room].get("monsters",[]):
        print(monsters[m], "in the room.\n")
        if monsters[m] == "an ogre":
            Monsters.ogre()
            break
    for i in rooms[room].get("items",[]):
        print(items[i], "in the room.")
    if (len(rooms[room].get("monsters",[])) + len(rooms[room].get("items",[]))) == 0: 
        print("nothing in the room.")
      
def transfer(from_, to_, prompt, error):
    if len(from_) != 0 :
        item = show_inventory(from_)
        while True:
            xfer = input("Choose > ").lower()
            if int(xfer) >= 0 and int(xfer) < len(from_):
                to_.append(from_[int(xfer)])
                del from_[int(xfer)]
                return item
                break
            else:
                print("Cannot do that ... ")
    else:
        print( error )
 
def show_inventory(inventory):
    for index, i in enumerate(inventory):
        print(str(index), items[i])
        return (items[i])

def stats(stats):
    time.sleep(2)
    print("\nLooking down at your forearm, shocked, you just stare at the numbers.")
    time.sleep(2)
    print("\nThe Voice comes back, 'These are your stats and they will either serve you well or not.'")
    print("\nHealth =", hp, "HP,", "Strength =", sp, "SP and", "Agility =", ap, "AP.")
 
#calls the main function
if __name__=="__main__":
    main()

