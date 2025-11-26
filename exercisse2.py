"""
exercise de

"""
import random
from dataclasses import dataclass


def roll_stat():
    de1 = random.randint(1,6)
    de2 = random.randint(1, 6)
    de3 = random.randint(1, 6)
    de4 = random.randint(1, 6)

    pass
@dataclass
class NPCStats:
    force: int = roll_stat()
    dexterite: int = random.randint(1,20)
    constitution: int = random.randint(1,20)
    inteligence: int = random.randint(1,20)
    sagesse: int = random.randint(1,20)
    charisme: int = random.randint(1,20)


