"""
Lars schougaard 406 exercice su les classes
"""
import math
import random


class StringFoo:
    def __init__(self):
        self.message = ""

    def set_string(self, msg):
        self.message = msg

    def print_string(self):

        print(self.message.upper())




"""
sf = StringFoo()


sf.set_string("obligation")
sf.print_string()
"""
class rectangle:
    def __init__(self, longueure, largeure):
        self.longueure = longueure
        self.largeure = largeure

    def calcul_aire(self):
        self.aire = self.largeure * self.longueure
        print(self.aire)
"""
banne = rectangle(3,4)

banne.calcul_aire()
"""

class cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        self.aire = self.rayon * self.rayon * math.pi
        print(self.aire)

    def calcul_circonférence(self):
        self.circonférence = 2 * math.pi * self.rayon
        print(self.circonférence)
"""
oven = cercle(6)
oven.calcul_aire()
oven.calcul_circonférence()
"""
class hero:
    def __init__(self,nom):
        self.nom = nom
        self.vie = random.randint(1,10) + random.randint(1,10)
        self.attaque = random.randint(1,6)
        self.defense = random.randint(1,6)
        print(self.nom,self.defense,self.attaque,self.vie)
    def faire_attaque(self):
        self.force_attaque = self.attaque + random.randint(1,6)
        print(self.force_attaque)
    def damage(self,degats):
        self.vie += self.defense - degats
        print(self.vie)
    def est_vivant(self):
        if (self.vie > 0) : True


bob = hero("bob")
bob.damage(5)
bob.est_vivant()

