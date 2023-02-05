from itertools import product
from typing import Dict, List, Tuple
import json

class Enemy:
    def __init__(self, hp: int, dmg: int, heading: int, position: int):

        self.hp = hp
        self.dmg = dmg
        self.heading = heading # 0 -- right, 1 - left
        self.position = position
    
    def __str__(self):
        return f"Enemy({self.hp}, {self.dmg}, {self.heading}, {self.position})"


class Structre:
    def __init__(self, name: str):
        name = name.lower()
        if name == "base":
            self.hp = 1
            self.dmg = 0
        elif name == "fence":
            self.hp = 20
            self.dmg = 0
        elif name == "trap":
            self.hp = 1e9
            self.dmg = 2
        elif name == "cannon":
            self.hp = 5
            self.dmg = 5
        elif name == "tower":
            self.hp = 3
            self.dmg = 3
        elif name == "free":
            self.hp = 1e9
            self.dmg = 0
        else:
            raise Exception("Unknown structure")
        self.name = name

    def __str__(self):
        return f"{self.name.capitalize()}({self.hp}, {self.dmg})"


def simulation(answer: str) -> Tuple[bool, int, int]:
    structures: List[Structre] = []
    for i in range(20):
        if answer[i] == 'B':
            structures.append(Structre('base'))
        elif answer[i] == 'F':
            structures.append(Structre('fence'))
        elif answer[i] == 'R':
            structures.append(Structre('trap'))
        elif answer[i] == 'C':
            structures.append(Structre('cannon'))
        elif answer[i] == 'T':
            structures.append(Structre('tower'))
        elif answer[i] == '=':
            structures.append(Structre('free'))
        else:
            raise Exception('Unknown structure')

    points = 0
    enemy = Enemy(int(1e9), 1, 0, 0)
    #only one healthy but weak enemy
    damage = 0
    while True:
        # 1. move all enemies
        if enemy.heading == 0:
            if enemy.position + 1 < 20:
                if structures[enemy.position + 1].name not in ('base', 'fence', 'cannon', 'tower'):
                    enemy.position += 1
            elif enemy.position + 1 >= 20:
                return True, points, damage
        elif enemy.heading == 1:
            if enemy.position - 1 >= 0:
                if structures[enemy.position - 1].name not in ('base', 'fence', 'cannon', 'tower'):
                    enemy.position -= 1
        # 2. make damage to player's structures
        if enemy.position + 1 < 20:
            structures[enemy.position + 1].hp -= enemy.dmg
            if structures[enemy.position + 1].hp <= 0:
                if structures[enemy.position + 1].name == "base":
                    return False, points, damage
                else:
                    structures[enemy.position + 1] = Structre('free')
        if enemy.position - 1 >= 0:
            structures[enemy.position - 1].hp -= enemy.dmg
            if structures[enemy.position - 1].hp <= 0:
                if structures[enemy.position - 1].name == "base":
                    return False, points, damage
                else:
                    structures[enemy.position - 1] = Structre('free')
        # 3. new enemies appear
        #remove apperaing stage
        #enemies.append(Enemy(hp, dmg, 0, 0))
        #enemies.append(Enemy(hp, dmg, 1, 19))
        # 4. make damage to enemy by trap
        if structures[enemy.position].name == "trap":
            enemy.hp -= structures[enemy.position].dmg
            damage += structures[enemy.position].dmg
        # 5. make damage to enemy by cannon/tower
        if enemy.position - 4 >= 0:
            if structures[enemy.position - 4].name == "tower":
                enemy.hp -= structures[enemy.position - 4].dmg
                damage += structures[enemy.position - 4].dmg
        if enemy.position - 3 >= 0:
            if structures[enemy.position - 3].name == "tower":
                enemy.hp -= structures[enemy.position - 3].dmg
                damage += structures[enemy.position - 3].dmg
        if enemy.position - 2 >= 0:
            if structures[enemy.position - 2].name in ("cannon", "tower"):
                enemy.hp -= structures[enemy.position - 2].dmg
                damage += structures[enemy.position - 2].dmg
        if enemy.position - 1 >= 0:
            if structures[enemy.position - 1].name in ("cannon", "tower"):
                enemy.hp -= structures[enemy.position - 1].dmg
                damage += structures[enemy.position - 1].dmg
        if enemy.position + 1 < 20:
            if structures[enemy.position + 1].name in ("cannon", "tower"):
                enemy.hp -= structures[enemy.position + 1].dmg
                damage += structures[enemy.position +1].dmg
        if enemy.position + 2 < 20:
            if structures[enemy.position + 2].name in ("cannon", "tower"):
                enemy.hp -= structures[enemy.position + 2].dmg
                damage += structures[enemy.position +2].dmg
        if enemy.position + 3 < 20:
            if structures[enemy.position + 3].name == "tower":
                enemy.hp -= structures[enemy.position + 3].dmg
                damage += structures[enemy.position + 3].dmg
        if enemy.position + 4 < 20:
            if structures[enemy.position + 4].name == "tower":
                enemy.hp -= structures[enemy.position + 4].dmg
                damage += structures[enemy.position + 4].dmg
        # 6. add point if all ok
        points += 1

alphabet = 'CFRT'
comb_dmg: Dict[str, int] = {}
for r in range(2, 6):
    perms = list(product(alphabet, repeat=r)) # type: ignore
    for perm in perms:
        structure = ''.join(perm)
        if len(structure) in (4, 5) and not structure.endswith('T'):
            continue
        answer = '=' + structure + '=' * (20 - 1 - len(structure))
        comb_dmg[structure] = simulation(answer)[2]
comb_dmg = {k: v for k, v in sorted(comb_dmg.items(), key=lambda item: item[1], reverse=True)}
with open('output.json', 'w') as outfile:
    json.dump(comb_dmg, outfile, indent=4)
