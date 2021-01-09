from item import Item, Weapon, Furniture

class Player():

    def __init__(self):
        self.strength = 10  # Will be changed, I'm sure.
        self.inventory = {}  # {}  MAYBE?

    def check_inventory(self):
        print("-----INVENTORY-----")
        for item in self.inventory:
            print(item)
            #print(self.inventory[item].describe())
        