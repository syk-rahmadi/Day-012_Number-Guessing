################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# local scope
def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()
#print(potion_strength)

# global scope
player_health = 10
def drink_potion():
  potion_strength = 2
  print(player_health)

drink_potion()
print(player_health)

# there is no block scope

game_level = 3
def create_enemy():
  enemies = ["Skeleton", "Zombie", "Alien"]
  if game_level < 5:
      new_enemy = enemies[0]
  print(new_enemy)

# Modify global scope
enemies = "skeleton"

def increase_enemies():
    enemies = "zombie"
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Constants

PI = 3.14
URL = "https://www.google.com"
TWITTER_HANDLE = "@jack"




