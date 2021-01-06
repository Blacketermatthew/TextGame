from item import Item, Weapon, Furniture

class Player():

    def __init__(self):
        self.strength = 10
        self.inventory = []

    def check_inventory(self):
        print("-----INVENTORY-----")
        for item in self.inventory:
            print(item)
        