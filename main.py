# TextBased RPG Program (Made by Ethan K, Michael B and Michael D)

# Imports
from random import randint, choice

# Global variables
# Player data
main_game_input = ""
player_name = ""
player_class = ""
player_health = 100
player_b_points = 0
player_heal_usage = 3
battle_won = 0
loop_count = 0
player_data = {"name": player_name, "health": player_health, "points": player_b_points, "class": player_class}
# Goblin data
goblin_data = {"name": "Goblin", "health": 32}
# Beat Farmer data
beat_farmer_data = {"name": "Beat Farmer", "health": 40}
# Babbo data
babbo_data = {"name": "Babbo", "health": 50}


# Battle logic
def battle():
    """
  Main battle sequence
  """
  # Variable initializations and imports
    enemy = choice(["Goblin", "Beat Farmer", "Babbo"])
    global player_heal_usage
    global player_b_points
    global player_health
    global battle_won
    global loop_count
    print "Enemy %s approaches!" % enemy

    # Main battle loop
    while True:
        # Random damage/heal initialization for each loop around
        battle_points = randint(50, 101)
        player_damage = randint(10, 21)
        goblin_damage = randint(5, 11)
        beat_farmer_damage = randint(10, 21)
        babbo_damage = randint(15, 26)
        player_heal_ability = [player_heal_usage, randint(10, 16)]

        # Show health each loop
        if enemy == "Goblin":
          if player_health <= 0:
            # Player defeated
              print "You have been defeated."
              player_health = 100
              player_heal_usage = 3
              goblin_data["health"] = 32
              return None  # Exits function
          else:
            print "\nYour health: {}, Enemy health: {}".format(player_health, goblin_data["health"])
        elif enemy == "Beat Farmer":
          if player_health <= 0:
            # Player defeated
              print "You have been defeated."
              player_health = 100
              player_heal_usage = 3
              beat_farmer_data["health"] = 40
              return None  # Exits function
          else:
            print "\nYour health: {}, Enemy health: {}".format(player_health, beat_farmer_data["health"])
        else:
          if player_health <= 0:
            # Player defeated
              print "You have been defeated."
              player_health = 100
              player_heal_usage = 3
              babbo_data["health"] = 50
              return None  # Exits function
          else:
            print "\nYour health: {}, Enemy health: {}".format(player_health, babbo_data["health"])

        action = raw_input("{}, choose your battle action (a - attack, h - heal, (3 heals per battle) e - escape): ".format(player_name))

        if enemy == "Goblin":
            # Health checks
            if goblin_data["health"] > 0 and player_health > 0:
                # Action logic for attack and heal
                if action == "a":
                    # Attack logic
                    goblin_data["health"] -= player_damage
                    print "{} took {} damage".format(goblin_data["name"], player_damage)
                elif action == "h":
                    # Heal logic
                    if player_heal_ability[0] < 1:
                        print "You ran out of heals for this battle!"
                    elif player_health >= 100:
                        print "You are already at max HP."
                    else:
                        player_health += player_heal_ability[1]
                        print "You healed {} HP.".format(player_heal_ability[1])
                    player_heal_usage -= 1
                elif action == "e":
                    print "You escaped the battle."
                    player_health = 100
                    player_heal_usage = 3
                    goblin_data["health"] = 32
                    return None  # Exits function
                else:
                    # Incorrect argument logic
                    print "Please enter either the right arguments."
                    continue
            # Defeat checks
            if goblin_data["health"] <= 0:
              # Enemy defeated
              print "You defeated the enemy. You got", battle_points, "battle points!"
              player_b_points += battle_points
              player_heal_usage = 3
              player_health = 100
              battle_won += 1
              goblin_data["health"] = 32
              return None  # Exits function
            elif player_health <= 0:
              # Player defeated
              print "You have been defeated."
              player_health = 100
              player_heal_usage = 3
              goblin_data["health"] = 32
              return None  # Exits function

        elif enemy == "Beat Farmer":
            # Health checks
            if beat_farmer_data["health"] > 0 and player_health > 0:
                # Action logic for attack and heal
                if action == "a":
                    # Attack logic
                    beat_farmer_data["health"] -= player_damage
                    print "{} took {} damage".format(beat_farmer_data["name"], player_damage)
                elif action == "h":
                    # Heal logic
                    if player_heal_ability[0] < 1:
                        print "You ran out of heals for this battle!"
                    elif player_health >= 100:
                        print "You are already at max HP."
                    else:
                        player_health += player_heal_ability[1]
                        print "You healed {} HP.".format(player_heal_ability[1])
                    player_heal_usage -= 1
                elif action == "e":
                    print "You escaped the battle."
                    player_health = 100
                    player_heal_usage = 3
                    beat_farmer_data["health"] = 40
                    return None  # Exits function
                else:
                    # Incorrect argument logic
                    print "Please enter either the right arguments."
            if beat_farmer_data["health"] <= 0:
              # Enemy defeated
              print "You defeated the enemy. You got", battle_points, "battle points!"
              player_b_points += battle_points
              battle_won += 1
              player_health = 100
              player_heal_usage = 3
              beat_farmer_data["health"] = 40
              return None  # Exits function
            elif player_health <= 0:
              # Player defeated
              print "You have been defeated."
              player_health = 100
              player_heal_usage = 3
              beat_farmer_data["health"] = 40
              return None  # Exits function

        else:
            # Health checks
            if babbo_data["health"] > 0 and player_health > 0:
                # Action logic for attack and heal
                if action == "a":
                    # Attack logic
                    babbo_data["health"] -= player_damage
                    print "{} took {} damage".format(babbo_data["name"], player_damage)
                elif action == "h":
                    # Heal logic
                    if player_heal_ability[0] < 1:
                        print "You ran out of heals for this battle!"
                    elif player_health >= 100:
                        print "You are already at max HP."
                    else:
                        player_health += player_heal_ability[1]
                        print "You healed {} HP.".format(player_heal_ability[1])
                elif action == "e":
                    print "You escaped the battle."
                    player_health = 100
                    player_heal_usage = 3
                    babbo_data["health"] = 50
                    return None  # Exits function
                else:
                    # Incorrect argument logic
                    print "Please enter either the right arguments."
            if babbo_data["health"] <= 0:
              # Enemy defeated
              print "You defeated the enemy. You got", battle_points, "battle points!"
              player_b_points += battle_points
              player_heal_usage = 3
              player_health = 100
              battle_won += 1
              babbo_data["health"] = 50
              return None  # Exits function
            elif player_health <= 0:
              # Player defeated
              print "You have been defeated."
              player_health = 100
              player_heal_usage = 3
              babbo_data["health"] = 50
              return None  # Exits function

        # Enemy attack checks
        if choice == "Goblin":
            player_health -= goblin_damage
            print "You took {} damage.".format(goblin_damage)
        elif choice == "Babbo":
            player_health -= babbo_damage
            print "You took {} damage.".format(babbo_damage)
        else:
            player_health -= beat_farmer_damage
            print "You took {} damage.".format(beat_farmer_damage)

        loop_count += 1


# Main game loop
print "Welcome to this Text-Based RPG Game!\nRegistration will now begin."
# Registration
player_name = raw_input("\nEnter your name: ")
player_class = raw_input("Enter your class (Knight, Mage, Cleric, Archer or Bandit): ")
print "Registration complete. The game will now begin!"
# Fix data formatting
player_data["name"] = "Name: " + str(player_name)
player_data["class"] = "Class: " + str(player_class).capitalize()
# Game start
while True:
  # Main imput
  main_game_input = raw_input("\nWhat do you want to do {}? (b - battle, s - show stats, e - end game) ".format(player_name))
  # Input checks
  if main_game_input == "b":
      battle()
  elif main_game_input == "s":
      # Updates point and health formatting each time the argument is run
      player_data["points"] = "Battle Points: " + str(player_b_points)
      player_data["health"] = "Health: " + str(player_health)
      for data in player_data.values():
        print data
  elif main_game_input == "e":
    print "Thanks for playing!"
    break
  else:
    print "Please enter the right arguments."