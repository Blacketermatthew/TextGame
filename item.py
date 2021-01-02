class Item():

    inventory = []

    def __init__(self, name):
        self.name = name
        self.description = None
        self.can_put_in_inventory = True
    
    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def set_description(self, item_description):
        self.description = item_description
    
    def get_description(self):
        return self.description

    def add_to_inventory(self):
        if self.can_put_in_inventory == True:
            print(f"You add {self.name} to your inventory.")
            Item.inventory.append(self)
        else:
            print("You cannot add this item to your inventory.")

    def check_inventory(self):
        print("-----INVENTORY-----")
        for item in Item.inventory:
            print(item.name)

    def check_item(self):
        print(self.can_put_in_inventory)


class Weapon(Item):
   def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage  # Damage can be 0-100

class Furniture(Item):
    def __init__(self, name):
        super().__init__(name)
        self.can_put_in_inventory = False
