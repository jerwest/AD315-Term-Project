import time
import random
from Stats import Stats
import sys

class Chasm:
    def chasmStart():
        time.sleep(2)
        print(" \n")
        time.sleep(1)
        print(" \n")
        time.sleep(1)
        print(" \n")
        time.sleep(1) 
        print("\n\nYou wake up in a deep chasm with no recollection of how you got there.\n")
        time.sleep(3)
        print("Heart pounding, you look around the earthen walls for a way out and see no escape.\n")
        time.sleep(3)
        print("Looking up, the opening is hundreds of feet above which gives way to stars in a clear sky.\n")
        time.sleep(4)
        print("Out of the corner of your eye, a soft, purple glow catches your attention.\n")
        time.sleep(3)
        print("It's coming from the top of a stone dais, in the middle of the chasm.\n")
        time.sleep(3)
        print("Strange...")
        time.sleep(1)
        print("...it wasn't there before.\n")
        time.sleep(2)
        print("Curious, you walk towards it and see that there are three - black, 20-sided die.\n")
        time.sleep(2)
        print("One with red glowing numbers, another glowing blue numbers and the third with white")
        print("glowing numbers.\n")

    ##  DETERMINES STATS POINTS
        decision = input("What do you do? 'Roll' or 'Ignore'? ").lower()
        while 1==1:
            if decision == "roll":
                value = "not scared"
                stats = Stats.allStats(value)
                break
            elif decision == "ignore":
                time.sleep(2)
                print("\nConfused about what is going on, you walk away from the dais, to better search the chasm.\n")
                time.sleep(3)
                print("Walking around the edges of the walls, you quickly realize that you are indeed trapped.\n")
                time.sleep(3)
                print("Slumping to the ground in despair, your head rests against the earthen wall and your eyes")
                print("once again fall on the glowing dice on the dais.\n")
                time.sleep(5)
                print("As if on cue, the glowing begins to pulsate and then in a hushed whisper you hear...\n")
                time.sleep(3)
                print("'Roll or die.'\n")
                time.sleep(2)
                print("The Voice gets louder...\n")
                time.sleep(1)
                print("'Roll or DIE.'\n")
                time.sleep(2)
                print("Getting even louder, it pushes you to obey...\n")
                time.sleep(1)
                print("'ROLL OR DIE!'\n")
                time.sleep(1)
                print("'ROLL OR DIE!'\n")
                time.sleep(1)
                print("'ROLL OR DIE!'\n")
                time.sleep(1)
                secondChance = input("What do you do? 'Roll' or 'Ignore'? ").lower()
                while 1==1:
                    if secondChance == "roll":
                        value = "scared"
                        stats = Stats.allStats(value)
                        break
                    elif secondChance == "ignore":
                        time.sleep(2)
                        print("\nYou're too scared and won't roll the dice, no matter what you hear.")
                        time.sleep(3)
                        print("\nThe Voice says...")
                        time.sleep(2)
                        print("...'your choice, now die!'")
                        time.sleep(2)
                        print("\nYour heart begins to ache as if someone is squeezing it.")
                        time.sleep(3)
                        print("\nThe pressure builds and the pain grows as your heart is squeezed harder and harder.")
                        time.sleep(3)
                        print("\nYour vision begins to darken with the loss of blood flow and then your heart explodes.")
                        time.sleep(3)
                        print("\nYou're dead!")
                        time.sleep(1)
                        print("\nThank you for playing 'The Chasm'... good-bye!")
                        sys.exit()
                    else:
                        secondChance = input("\nMust type either, 'Roll' or 'Ignore'. ").lower()
                break
            else:
                decision = input("\nMust type either, 'Roll' or 'Ignore'. ").lower()
        return stats
