from item import Item, Weapon, Furniture

class Player():

    def __init__(self):
<<<<<<< HEAD
        self.strength = 10
        self.inventory = []
=======
        self.strength = 10  # Will be changed, I'm sure.
        self.inventory = {}  # {}  MAYBE?
>>>>>>> Insult/Fight-tests

    def check_inventory(self):
        print("-----INVENTORY-----")
        for item in self.inventory:
            print(item)
<<<<<<< HEAD
=======
            #print(self.inventory[item].get_description())
>>>>>>> Insult/Fight-tests
        