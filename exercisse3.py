"""
exercisse 3 lars schougaard 406
"""
from dataclasses import dataclass
from enum import Enum
import random

def roll_stat():
    stats = [random.randint(1, 6) for x in range(4)]
    stats.sort(reverse=True)
    stats.pop()
    return sum(stats)

class Alignement(Enum):

    LAWFUL_GOOD = 0
    NEUTRAL_GOOD = 1
    CHAOTIC_GOOD = 2
    LAWFUL_NEUTRAL = 3
    NEUTRAL = 4
    CHATIC_NEUTRAL = 5
    LAWFUL_EVIL = 6
    NEUTRAL_EVIL = 7
    CHAOTIC_EVIL = 8
    UNDEFINED = 9

@dataclass
class NPCStats:

    force: int = roll_stat()
    dexterite: int = roll_stat()
    constitution: int = roll_stat()
    inteligence: int = roll_stat()
    sagesse: int = roll_stat()
    charisme: int = roll_stat()
@dataclass
class Item:
    quantite: int
    nom: str


class SacADos:
    def __init__(self):
        self.liste_item = []

    def ajouter_item(self, item_ajouter: Item):
        for item in self.liste_item:
            if item.nom == item_ajouter.nom:
                # existe dans la liste...
                item.quantite += item_ajouter.quantite
            else
                self.liste_item.append(item_ajouter)

    def retire_item(self, item_ajouter: Item):
        for item in self.liste_item:
            if item.nom == item_ajouter.nom:
                item.quantite -= item_ajouter.quantite
            if item.quantite < 0

                print("l'item nes pas dans le sac a dos")


sad = SacADos()
sad.ajouter_item(Item(2, "or"))
sad.ajouter_item(Item(20, "argent"))
sad.ajouter_item(Item(20, "or"))
print(sad.liste_item)


class NPC:

    def __init__(self,nom,race="",espece="",profession=""):
        self.Stats = NPCStats()
        self.armure = random.randint(1,12)
        self.nom = nom
        self.race = race
        self.espece = espece
        self.PTvie = random.randint(1,20)
        self.profession = profession
        self.alignement = Alignement.LAWFUL_GOOD

    def afficher_caracteristique(self):
        print(self.Stats)
        print(f"nom:{self.nom}")
        print(f"espece:{self.espece}")
        print(f"race:{self.race}")
        print(f"Point de vie :{self.PTvie}")
        print(f"profession:{self.profession}")
        print(f"armure:{self.armure}")

    def est_vivant(self):
        return self.PTvie > 0

class Kobold(NPC):
    def __init__(self,nom, profession):
        super().__init__(nom,profession)
        self.race = "Kobold"


    def attaquer(self,cible):
        attack_value = random.randint(1,20)
        if attack_value == 20:
            cible.subir_dommage(random.randint(1, 8))
        elif attack_value == 1:
            print("Le coup n'a pas fonctioner")
        else:
            if attack_value < cible.armure:
                print("Le coup n'a pas fonctioner")
            else:
                cible.subir_dommage(random.randint(1, 8))
        print(attack_value)

    def subir_dommage(self,degats):
        self.PTvie -= degats


class Hero(NPC):
    def __init__(self, nom, profession):
        super().__init__(nom, profession)
        self.race = "Hero"

    def attaquer(self, cible):
        attack_value = random.randint(1, 20)
        if attack_value == 20:
            cible.subir_dommage(random.randint(1, 8))
        elif attack_value == 1:
            print("Le coup n'a pas fonctioner")
        else:
            if attack_value < cible.armure:
                print("Le coup n'a pas fonctioner")
            else:
                cible.subir_dommage(random.randint(1, 8))
        print(attack_value)


    def subir_dommage(self, degats):
        self.PTvie -= degats



H = Hero("H",  "warrior")
k = Kobold("k",  "warrior")

k.attaquer(H)

bob = Hero("bob", "sorcier")
bob.subir_dommage(5)
if bob.est_vivant():
    print("Il est vivant!")