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

    def __init__(self,nom,race="",espece="",profession=""):
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

