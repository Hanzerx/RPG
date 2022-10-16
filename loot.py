import random


def loot(monster_level, healing_potion, luck_potion):
    # Gold
    gold_random_int = random.randint(0, 9)
    if gold_random_int == 0:
        gold_random_int = 1
    gold = gold_random_int * monster_level
    print(f"Looted {gold} gold.")
    # Healing potions
    healing_potion_random_int = random.randint(0, 2)
    if healing_potion_random_int == 2:
        healing_potion += 1
        print("Looted healing potion")
    # Weapons
    # weapon_random_int = random.randint(0, 9)
    # Armor
    # armor_random_int = random.randint(0, 9)
    # Lucky potions
    luck_potion_random_int = random.randint(0, 50)
    if luck_potion_random_int == 0:
        luck_potion += 1
        print("Looted luck potion")
    return gold, healing_potion, luck_potion
