import room as rm

class Item():

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
        print(self.description)


class Weapon(Item):
   def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage  # Damage can be 0-100

class Furniture(Item):
    def __init__(self, name):
        super().__init__(name)
        self.can_put_in_inventory = False
