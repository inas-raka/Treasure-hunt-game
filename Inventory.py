class Inventory:
    def __init__(self, capacity):
        """Initializes the inventory with a given capacity."""
        self.capacity = capacity  # Maximum number of items the player can carry
        self.items = {}  # Dictionary to store items with their quantities
    
    def add_item(self, item, quantity=1):
        """Adds a specified quantity of an item to the inventory."""
        if len(self.items) >= self.capacity:
            print("Inventory is full! Cannot add more items.")
        else:
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity
            print(f"{quantity} {item}(s) added to inventory.")
    
    def remove_item(self, item, quantity=1):
        """Removes a specified quantity of an item from the inventory."""
        if item in self.items:
            if self.items[item] >= quantity:
                self.items[item] -= quantity
                if self.items[item] == 0:
                    del self.items[item]
                print(f"{quantity} {item}(s) removed from inventory.")
            else:
                print(f"Not enough {item}(s) to remove.")
        else:
            print(f"{item} not found in inventory.")
    
    def view_inventory(self):
        """Displays all items and their quantities in the inventory."""
        if self.items:
            print("Inventory:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")
        else:
            print("Inventory is empty.")
    
    def is_full(self):
        """Returns whether the inventory is full."""
        return len(self.items) >= self.capacity

# Example Usage
player_inventory = Inventory(capacity=5)

# Add items
player_inventory.add_item("Potion", 3)
player_inventory.add_item("Sword", 1)
player_inventory.add_item("Shield", 1)

# View inventory
player_inventory.view_inventory()

# Remove items
player_inventory.remove_item("Potion", 2)

# View updated inventory
player_inventory.view_inventory()

# Try adding more items when the inventory is full
player_inventory.add_item("Bow", 1)
player_inventory.add_item("Arrow", 5)