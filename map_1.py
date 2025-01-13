import random
import time

# Constants for map dimensions
MAP_WIDTH = 15
MAP_HEIGHT = 10
NUM_ENEMIES = 3  # Number of enemies to spawn
NUM_CHESTS = 1   # Number of chests to spawn

# Tile types
TILE_EMPTY = ' '
TILE_GRASS = ' '
TILE_WATER = ' '
TILE_WALL = '|'
TILE_ENEMY = 'E'
TILE_CHEST = 'C'
TILE_EXIT = 'X'

# Item types and their properties
ITEMS = {
    'Sword': {'type': 'Weapon', 'damage': random.randint(16, 28)},
    'Bow': {'type': 'Weapon', 'damage': random.randint(9, 17)},
    'Shield': {'type': 'Armor', 'damage': 0},
    'Mace': {'type': 'Weapon', 'damage': random.randint(13, 20)},
    'Health Potion': {'type': 'Healing', 'heal': random.randint(14, 26)},
    'Mana Potion': {'type': 'Mana', 'heal': random.randint(5, 15)},
    'Gold': {'type': 'Currency', 'amount': random.randint(8, 50)},
    'Key': {'type': 'Key', 'amount': 1}
}

# Enemy types and their damage values
ENEMY_TYPES = {
    'Goblin': {'damage': random.randint(18, 27)},
    'Rebel': {'damage': random.randint(11, 31)},
    'Evil Police': {'damage': random.randint(20, 44)},
    'Orc': {'damage': random.randint(16, 39)},
    'Troll': {'damage': random.randint(14, 32)}
}

# Map names for each level
MAP_NAMES = [
    "SHQIPRIA --- \n Welcome to SHQIPRIA\n Be careful\n Here you can find SWORDS,HELMETS but also GUARDS!\n You will first face KRUJE then move onto the center TIRANA",
    "DARDANIA ---\n Welcome to DARDANIA\n Be careful\n Here you can find AXES,CHESTPLATES but also REBELS!\n You will first face the city of KACANIK then move onto the center PRISHTINA",
    "ILIRDIA --- Welcome to ILIRDIA\n Be careful\n Here you can find BOWS,LEGGINGS but also EVIL POLICE!\n You will first face KUMANOVO then move onto the center SHKUP\n ",
    "MAL I ZI --- \n Welcome to MAL I ZI\n Be careful\n Here you can find MACES,BOOTS but also HYENAS!\n You will first face the beaches of ULQIN then move onto the center BUDVA",
    "CAMERIA --- \n Welcome to CAMERIA\n Be careful\n Here you can find SPEARS,SHIELDS but also THIEVES!\n You will first face LELOVA then move onto the center KONSIPOL"
]

# Class definition for Player
class Player:
    def __init__(self, player_class):
        self.player_class = player_class
        self.health = 100
        self.damage = 10
        self.special_ability = ""
        self.armor = 0
        self.inventory = []

        if self.player_class == 'Warrior':
            self.health += 30
            self.damage += 10
            self.special_ability = "Charge Attack"
        elif self.player_class == 'Archer':
            self.health += 10
            self.damage += 7
            self.special_ability = "Piercing Shot"
        elif self.player_class == 'Mage':
            self.health += 20
            self.damage += 5
            self.special_ability = "Fireball"
        elif self.player_class == 'Thief':
            self.health += 15
            self.damage += 6
            self.special_ability = "Stealth"

    def display_info(self):
        print(f"\nClass: {self.player_class}")
        print(f"Health: {self.health}")
        print(f"Damage: {self.damage}")
        print(f"Special Ability: {self.special_ability}")
        print(f"Inventory: {self.inventory}")


# Function to generate a random game map with enemies and chests
def generate_map():
    game_map = []
    tile_choices = [TILE_GRASS,TILE_EMPTY,TILE_EMPTY, TILE_WATER, TILE_EMPTY, TILE_WALL]

    # Generate the map
    for y in range(MAP_HEIGHT):
        row = [random.choice(tile_choices) for _ in range(MAP_WIDTH)]
        game_map.append(row)

    # Place enemies randomly
    placed_enemies = 0
    enemy_positions = []
    while placed_enemies < NUM_ENEMIES:
        x, y = random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)
        if game_map[y][x] == TILE_EMPTY:
            enemy_type = random.choice(list(ENEMY_TYPES.keys()))
            game_map[y][x] = TILE_ENEMY
            enemy_positions.append((x, y, enemy_type))
            placed_enemies += 1

    # Place chests randomly
    placed_chests = 0
    while placed_chests < NUM_CHESTS:
        x, y = random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)
        if game_map[y][x] == TILE_EMPTY:
            game_map[y][x] = TILE_CHEST
            placed_chests += 1

    # Place the exit randomly
    x, y = random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)
    while game_map[y][x] != TILE_EMPTY:
        x, y = random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)
    game_map[y][x] = TILE_EXIT

    return game_map, enemy_positions


# Function to display the map with the player's current position
def display_map(game_map, player_x, player_y):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if x == player_x and y == player_y:
                print("P", end=" ")  # Represent the player as 'P'
            else:
                print(game_map[y][x], end=" ")
        print()


# Function for combat interactions
def combat(enemy_name, enemy_damage, player):
    print(f"A wild {enemy_name} appears! It deals {enemy_damage} damage!")
    action = input("Do you want to fight or flee? (F/Fight or Q/Flee): ").upper()

    if action == 'F':
        player.health -= enemy_damage
        print(f"You fought bravely, but you took {enemy_damage} damage. Your health is now {player.health}.")
        if player.health <= 0:
            print(f"{enemy_name} has defeated you!")
            return False
        print(f"{enemy_name} has been defeated!")
        return True
    elif action == 'Q':
        print("You decided to flee!")
        return False
    return True


# Function for opening a chest and displaying its contents
def open_chest():
    dropped_items = random.sample(list(ITEMS.keys()), 3)  # Random 3 items
    print(f"You found a chest! It contains:")
    for idx, item in enumerate(dropped_items, start=1):
        item_info = ITEMS[item]
        print(f"{idx}. {item} - {item_info['type']}")
        if 'damage' in item_info:
            print(f"  Damage: {item_info['damage']}")
        if 'heal' in item_info:
            print(f"  Heal: {item_info['heal']}")
    return dropped_items


# Function to handle chest item selection
def select_items_from_chest(items):
    selected_items = []
    while items:
        print("\nItems in chest:")
        for idx, item in enumerate(items, start=1):
            print(f"{idx}. {item}")
        
        selection = input(f"Select an item to take (1-{len(items)}) or 'Q' to stop taking items: ").upper()
        if selection == 'Q':
            break
        try:
            idx = int(selection) - 1
            if 0 <= idx < len(items):
                selected_items.append(items[idx])
                print(f"You selected: {items[idx]}")
                items.pop(idx)
            else:
                print(f"Invalid selection. Choose a number between 1 and {len(items)}.")
        except ValueError:
            print("Invalid input. Please enter a number or 'Q' to stop.")
    
    return selected_items

# Function to type out the intro storyline
def type_out_storyline():
    intro_text = """In a world filled with conflict, war has ravaged the land. 
    The ancient kingdoms are torn apart, and only the bravest of souls dare to venture into the heart of battle. 
    Dark forces have emerged from the shadows, threatening to enslave the land and its people. 
    But hope remains. You, a warrior of destiny, must rise to the challenge and unite the broken world once again.
    
    Dear traveller...\n You have stepped into the eagles domain\n You must naviagte around a series of mazes\n Along the way you will find items treasure or... your worst enemy\n Be careful of your next step
    Choose your path, brave soul. Choose your class.
    """
    for char in intro_text:
        print(char, end='', flush=True)
        time.sleep(0.05)  # Delay to simulate typing effect
    print("\n")  # New line after the story is finished typing

# Main game loop
def main():
    # Class selection
    print("Welcome to the game!")
    print("Select your class:")
    print("1. Warrior")
    print("2. Archer")
    print("3. Mage")
    print("4. Thief")
    class_choice = input("Enter the number of your class choice: ")

    if class_choice == '1':
        player_class = 'Warrior'
    elif class_choice == '2':
        player_class = 'Archer'
    elif class_choice == '3':
        player_class = 'Mage'
    elif class_choice == '4':
        player_class = 'Thief'
    else:
        print("Invalid choice! Defaulting to Warrior.")
        player_class = 'Warrior'

    player = Player(player_class)
    player.display_info()  # Display player info

    # Main game loop
    game_over = False
    while not game_over:
        # Generate the game map for the current level
        game_map, enemy_positions = generate_map()

        # Player starting position
        player_x = MAP_WIDTH // 2
        player_y = MAP_HEIGHT // 2

        # Loop for level play
        while True:
            display_map(game_map, player_x, player_y)

            # Check if the player stepped on an enemy
            for (ex, ey, enemy_name) in enemy_positions:
                if ex == player_x and ey == player_y:
                    defeated = combat(enemy_name, ENEMY_TYPES[enemy_name]['damage'], player)
                    if defeated:
                        enemy_positions.remove((ex, ey, enemy_name))
                    break

            # Ask for user input to move the player or view stats
            move = input("Enter move (W/A/S/D to move, I for inventory, Q to quit): ").upper()

            if move == 'Q':
                print("You quit the game!")
                game_over = True
                break

            if move == 'I':
                player.display_info()

            # Movement logic
            new_x, new_y = player_x, player_y
            if move == 'W' and player_y > 0:
                new_y -= 1
            elif move == 'S' and player_y < MAP_HEIGHT - 1:
                new_y += 1
            elif move == 'A' and player_x > 0:
                new_x -= 1
            elif move == 'D' and player_x < MAP_WIDTH - 1:
                new_x += 1

            target_tile = game_map[new_y][new_x]

            if target_tile == TILE_WALL:
                print("Cannot move there! Wall in the way.")
            elif target_tile == TILE_CHEST:
                print("You found a chest!")
                items = open_chest()
                selected_items = select_items_from_chest(items)
                player.inventory.extend(selected_items)
                player_x, player_y = new_x, new_y
            elif target_tile == TILE_EXIT:
                print("You reached the exit! Moving to the next map.")
                break  # Exit to next level or map
            else:
                player_x, player_y = new_x, new_y

            if player.health <= 0:
                print("You have died. Game Over!")
                game_over = True
                break


if __name__ == "__main__":
    main()
