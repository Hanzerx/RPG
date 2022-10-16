import random
from RPG.loot import loot


def bird(position_increment):
    counter = 0
    attempt = 0
    lucky_fairy_random_amount = 50
    player_parameters = {
        "position_x": 50,
        "position_y": 50,
        "health": 25,
        "poisoned": False,
        "cursed": False,
        "frozen": False,
        "burning": False,
        "lucky": False,
        "drowning": False,
        "level": 1,
        "inventory": {
            "gold": 0,
            "healing_potion": 2,
            "luck_potion": 0,
        }
    }
    inventory = player_parameters["inventory"]
    gold = inventory["gold"]
    healing_potion = inventory["healing_potion"]
    luck_potion = inventory["luck_potion"]
    enemy_parameters = {
        "enemy_health": 20,
        "enemy_level": 1,
        "enemy_min_attack": 0,
        "enemy_max_attack": 10
    }
    potions = {
        "health": 10
    }

    grid = {"position_x": 100, "position_y": 100}
    while True:
        print("Your current position is \n"
              "x=", player_parameters["position_x"], " y=", player_parameters["position_y"])
        print(f"Health: {player_parameters['health']}")
        lucky_fairy = random.randint(0, lucky_fairy_random_amount)
        if lucky_fairy == 3:

            print("Random event: Fairy godmother appeared out of nowhere and offered "
                  "to heal you or lets you toss a coin, if it hits heads twice, she will give 10 gold")
            fairy_input = input("Choose heal or coin: ")
            if fairy_input == "heal":
                player_parameters["health"] += 5
                print("Fairy healed you for 5 points and your current health is: ", player_parameters["health"])
            elif fairy_input == "coin":
                coin_count = 0
                while coin_count <= 0:
                    coin_1 = random.randint(0, 1)
                    print(f"Coin 1 : {coin_1}")
                    coin_2 = random.randint(0, 1)
                    print(f"Coin 2 : {coin_2}")
                    coin_count += 1
                    if coin_1 + coin_2 == 2:
                        player_parameters["gold"] = 10
                        print(f"You won the coin toss. Your current gold amount is : {player_parameters['gold']}")
                    else:
                        print("You were unlucky.")
        vastus = input("Enter 1 to go up 2 to go down, 3 to go left, 4 to go right:")
        if (player_parameters["position_x"] >= 100) and (vastus == "4"):
            print("Unable to move, you are on the killer border, "
                  "move again in the same direction and you will get damaged")
            if attempt >= 1:
                player_parameters["health"] -= 1
            attempt += 1
            player_parameters["position_x"] = 100

        elif (player_parameters["position_x"] <= 0) and (vastus == "3"):
            print("Unable to move, you are on the killer border, "
                  "move again in the same direction and you will get damaged")
            player_parameters["position_x"] = 0
            if attempt >= 1:
                player_parameters["health"] -= 1
            attempt += 1

        elif (player_parameters["position_y"] <= 0) and (vastus == "2"):
            print("Unable to move, you are on the killer border, "
                  "move again in the same direction and you will get damaged")
            player_parameters["position_y"] = 0
            if attempt >= 1:
                player_parameters["health"] -= 1
            attempt += 1
        elif (player_parameters["position_y"] >= 100) and (vastus == "1"):
            print("Unable to move, you are on the killer border, "
                  "move again in the same direction and you will get damaged")
            player_parameters["position_y"] = 100
            if attempt >= 1:
                player_parameters["health"] -= 1
            attempt += 1
        elif vastus == "1":
            print("Moved up")
            player_parameters["position_y"] += position_increment

        elif vastus == "2":
            print("moved down")
            player_parameters["position_y"] -= position_increment

        elif vastus == "3":
            print("moved Left")
            player_parameters["position_x"] -= position_increment

        elif vastus == "4":
            print("moved right")
            player_parameters["position_x"] += position_increment

        elif vastus == "inv":
            print(f"Items in inventory:\n"
                  f"Gold: {gold}\n"
                  f"Health potions: {healing_potion}\n"
                  f"Luck potions: {luck_potion}\n")

        elif vastus == "heal":
            if healing_potion > 0:
                print(f"Healed for {potions['health']}")
                player_parameters["health"] += potions["health"]
                healing_potion -= 1
            else:
                print("Sorry, you are out of healing potions")

        # elif vastus == "a":
        #     print("you attacked enemy", enemy_parameters["enemy_health"])
        #     enemy_parameters["enemy_health"] -= 5
        #     if enemy_parameters["enemy_health"] <= 0:
        #         print("You have killed the enemy")
        # Random enemy
        enemy_spawn = random.randint(0, 2)
        if enemy_spawn == 0:
            enemy_parameters["enemy_health"] = 10
            while enemy_parameters["enemy_health"] > 0:
                encounter_increment = 0
                if encounter_increment <= 0:
                    enemy_option = input(
                        f"You have stumbled on an KILLER ORC. Your current health is: {player_parameters['health']} "
                        "\n You can 'Flee', 'Attack' or 'Heal'")
                else:
                    enemy_option = input("You can 'Flee', 'Attack' or 'Heal'")
                encounter_increment += 1
                enemy_attack = False
                if enemy_option == "flee":
                    flee_chance = random.randint(0, 1)
                    if flee_chance == 0:
                        print("You were unsuccessful")
                        attack_chance = random.randint(0, 2)
                        if attack_chance == 1:
                            enemy_damage = random.randint(
                                enemy_parameters["enemy_min_attack"],
                                enemy_parameters["enemy_max_attack"]
                            )
                            print(f"The KILLER ORC attacked you for {enemy_damage}")
                            player_parameters["health"] -= enemy_damage
                    else:
                        print("You were successful and got away from the KILLER ORC")
                        enemy_spawn = 1
                        return enemy_spawn
                    enemy_parameters["enemy_health"] = 0
                elif enemy_option == "attack":
                    player_attack_chance = random.randint(0, 9)
                    if player_attack_chance >= 0:
                        player_attack_damage = random.randint(0, 4 * player_parameters["level"])
                        if player_attack_damage == 0:
                            print("You missed")
                        else:
                            if enemy_parameters["enemy_health"] <= player_attack_damage:
                                print("You killed the KILLER ORC")
                                # Loot collection
                                print(inventory)
                                loot_collect = loot(1, healing_potion, luck_potion)
                                gold += loot_collect[0]
                                healing_potion += loot_collect[1]
                                luck_potion += loot_collect[2]
                                enemy_spawn = 1
                                return enemy_spawn
                            else:
                                enemy_parameters["enemy_health"] -= player_attack_damage
                                print(f"You hit the KILLER ORC for {player_attack_damage}. "
                                      f"KILLER ORC health: {enemy_parameters['enemy_health']}")
                elif enemy_option == "heal":
                    if healing_potion > 0:
                        player_parameters["health"] += 10
                    else:
                        print("You don't have any potions")
        elif vastus == "map":
            print("Here should be the map")
        # else:
        #     print("Error")

        # END
        print(inventory)
        if player_parameters["health"] <= 0:
            print("Game over, you have bleed out and died")
            break


bird(10)
