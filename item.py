class Item():

    def __init__(self, name):
        self.name = name
        self.description = None
    
    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def set_description(self, item_description):
        self.description = item_description
    
    def get_description(self):
        return self.description


class Weapon(Item):
   def __init__(self, name, damage):
       super().__init__(name)
       self.damage = damage  # Damage can be 0-100
