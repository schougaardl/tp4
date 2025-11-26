"""
Lars schougaard 406 exercice su les classes
"""
import math
import random
from dataclasses import dataclass

class StringFoo:
    def __init__(self):
        self.message = ""

    def set_string(self, msg):
        self.message = msg

    def print_string(self):

        print(self.message.upper())





sf = StringFoo()


sf.set_string("obligation")
sf.print_string()

class Rectangle:
    def __init__(self, longueure, largeure):
        self.longueure = longueure
        self.largeure = largeure

    def calcul_aire(self):
        self.aire = self.largeure * self.longueure
        print(self.aire)

banne = Rectangle(3,4)

banne.calcul_aire()


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        self.aire = self.rayon * self.rayon * math.pi
        print(self.aire)

    def calcul_circonférence(self):
        self.circonférence = 2 * math.pi * self.rayon
        print(self.circonférence)

oven = Cercle(6)
oven.calcul_aire()
oven.calcul_circonférence()


@dataclass
class NPCStats:
    force: int = random.randint(1,20)
    dexterite: int = random.randint(1,20)
    constitution: int = random.randint(1,20)
    inteligence: int = random.randint(1,20)
    sagesse: int = random.randint(1,20)
    charisme: int = random.randint(1,20)

class Hero:
    def __init__(self,nom):
        self.nom = nom
        self.vie = random.randint(1,10) + random.randint(1,10)
        self.attaque = random.randint(1,6)
        self.defense = random.randint(1,6)
        self.stats = NPCStats()

    def faire_attaque(self):
        return self.attaque + random.randint(1,6)

    def damage(self,degats):
        self.vie += self.defense - degats
        print(self.vie)
    def est_vivant(self):
        return self.vie > 0



bob = Hero("bob")
bob.damage(5)
if bob.est_vivant():
    print("Il est vivant!")

print(bob.stats)


