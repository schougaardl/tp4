"""
exercise de

"""
import random
from dataclasses import dataclass


def roll_stat():
    stats = [random.randint(1, 6) for x in range(4)]
    stats.sort(reverse=True)
    stats.pop()
    return sum(stats)

@dataclass
class NPCStats:

    force: int = roll_stat()
    dexterite: int = roll_stat()
    constitution: int = roll_stat()
    inteligence: int = roll_stat()
    sagesse: int = roll_stat()
    charisme: int = roll_stat()

class NPC:

    def __init__(self,nom,race,espece,profession):
        self.Stats = NPCStats()
        self.armure = random.randint(1,12)
        self.nom = nom
        self.race = race
        self.espece = espece
        self.PTvie = random.randint(1,20)
        self.profession = profession
    def afficher_caracteristique(self):
        print(self.Stats)
        print(f"nom:{self.nom}")
        print(f"espece:{self.espece}")
        print(f"race:{self.race}")
        print(f"Point de vie :{self.PTvie}")
        print(f"profession:{self.profession}")
        print(f"armure:{self.armure}")


bob = NPC("bob","arienne","humain","docteur")
bob.afficher_caracteristique()

class Kobold :
    def __init__(self):
        self.kobold_stats = NPC()

