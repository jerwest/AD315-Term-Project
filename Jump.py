import time
import random
from Stats import Stats

class Jump:
    def dieRoll():
        roll = random.randint(1, 6)
        return roll

    def totalOfDie():
        first_die = Jump.dieRoll()
        print("Die #1:", first_die)
        second_die = Jump.dieRoll()
        print("Die #2:", second_die)
        diceTotal = first_die + second_die
        return diceTotal       

    def jumpPit():
        time.sleep(1)
        print("Entering the door, you see a long hallway but you're unable to walk down it, due to a pit")
        print("in the floor with spikes at the bottom.")
        time.sleep(4)
        print("\nThe voice speaks again, saying, 'You must jump the pit, roll the dice to see if you can")
        print("clear it and land safely on the other side.'")
        time.sleep(4)
        print("\nTwo six-sided dice appear in the air before you, floating.")
        time.sleep(2)
        print("\n'Your agility plus the total of the dice must be higher than '31' to succeed.'")
        time.sleep(2)


