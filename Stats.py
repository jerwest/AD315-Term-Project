import time
import random


class Stats:
    def allStats(value):
        stats = []
        for i in range(3):
            stats.append(random.randrange(10,21))
        if value == "not scared":
            time.sleep(2)
            print("\nAgainst your better judgement, you decide to roll the dice.\n")
        elif value == "scared":
            time.sleep(2)
            print("\nScared, you run over to the dais, to roll the dice.\n")
        time.sleep(3)
        print("Taking them in one hand, you quickly drop them as they're searing hot and burn your hand.\n")
        time.sleep(3)
        print("They fall to the dais, tumbling around without a sound.")
        time.sleep(3)
        print("\nThe red glowing die comes up '" + str(stats[0]) + "', the blue '" + str(stats[1]) + "' and the white '" + str(stats[2]) + "'.")
        time.sleep(3)
        print("\nA needling pain suddenly comes from your left wrist and you see the number '" + str(stats[0]) + "' being")
        print("etched into your skin along with the letters 'HP'.\n")
        time.sleep(5)
        print("The pain continues as the rest of the numbers appear vertically down your forearm.")
        print("'" + str(stats[1]) + "' with 'SP' after it and '" + str(stats[2]) + "' with 'AP' after.")
        time.sleep(5)        
        if value == "not scared":
            print("\nIn a hushed whisper you hear, 'These are your stats. HP is health, SP is strength and AP")
            print("is agility. Be careful, once HP reaches '0' you're dead.'")
            time.sleep(5)  
            return stats
        elif value == "scared":
            print("\nThe hushed Voice returns, 'These are your stats. HP is health, SP is strength and AP")
            print("is agility. Be careful, once HP reaches '0' you're dead.'")
            time.sleep(5)  
            return stats

    def minusHealth(stats, value):
        stats = [stats[0] - value, stats[1], stats[2]]
        return stats

    def addHealth(stats, value):
        stats = [stats[0] + value, stats[1], stats[2]]
        return stats

    def minusStrength(stats, value):
        stats = [stats[0], stats[1] - value, stats[2]]
        return stats

    def addStrength(stats, value):
        stats = [stats[0], stats[1] + value, stats[2]]
        return stats

    def minusAgility(stats, value):
        stats = [stats[0], stats[1] - value, stats[2]]
        return stats

    def addAgility(stats, value):
        stats = [stats[0], stats[1] + value, stats[2]]
        return stats
