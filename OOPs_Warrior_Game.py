""" Sam attacks Paul and deals 9 damage
paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has died and Sam is victorious
Game Over


@samarjit_debnath

Src: Derek Banas
"""

import math
import random


# *************** Algorithm ******************

# Warrior &  Battle class

# Warriors will have names, health, attack and block maximums

# They  will have the capabilities to attack and block random amounts

# Attack random() 0.0 to 1.0 * maxAttack + .5

# Block will use random()

# Battle Class capability of looping until 1 warrior dies

# Warriors wil each get a turn  to attack each other

# Function gets 2 Warriors

# 1 Warrior attacks the other

# Attacks and Blocks are integers


class Warrior:

    def __init__(self, name="Warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() + .5)
        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)
        return blockAmt


class Battle:

    def startFight(self, warrior1, warrior2):
        print("\n********* Fight *******\n")
        while True:
            if self.getAttackResult(warrior1, warrior2) == "GAME OVER":
                print("GAME OVER")
                break

            if self.getAttackResult(warrior2, warrior1) == "GAME OVER":
                print("GAME OVER")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):

        warriorAAttkAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.block()
        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
        warriorB.health = warriorB.health - damage2WarriorB

        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage2WarriorB))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has died and {} is victorious".format(warriorB.name, warriorA.name))
            return "GAME OVER"

        else:
            return "Fight Again"


if __name__ == '__main__':
    maximus = Warrior("Maximus", 50, 20, 10)
    alexander = Warrior("Alexander", 50, 20, 10)
    battle = Battle()
    battle.startFight(maximus, alexander)






