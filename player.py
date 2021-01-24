from item import Item, Weapon, Furniture

class Player():

    def __init__(self):
        self.strength = 10  # Will be changed, I'm sure.
        self.inventory = {}  # {}  MAYBE?
        self.money_in_hand = 0

    def check_inventory(self):
        print("-----INVENTORY-----")
        print(f"Cash: ${self.money_in_hand}")
        for item in self.inventory:
            print(item)
            #print(self.inventory[item].describe())
        

you = Player()