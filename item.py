import room as rm
import player


class Item():

    def __init__(self, name):
        self.name = name
        self.description = None
        self.can_put_in_inventory = True

    def __str__(self):
        return 'Item %s - %s' % (self.name, self.description)
    
    # def set_name(self, item_name):
    #     self.name = item_name

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

    def __str__(self):
        return 'Weapon %s - %s' % (self.name, self.description)

class Furniture(Item):
    def __init__(self, name, money_contained=0):
        super().__init__(name)
        self.can_put_in_inventory = False
        self.money_contained = money_contained  # Sometimes items have cash in/on them

    def __str__(self):
        return 'Furniture %s - %s' % (self.name, self.description)

    # NEEDS TO BE WORKED ON.  PUT PLAYER FROM MAIN INTO PLAYER FILE
    def take_money(self):
        if self.money_contained > 0:
            print(f"You found ${self.money_contained}!")
            
            player.you.money_in_hand += self.money_contained
            self.money_contained = 0 # Removes the money from the item so you can't continuously spawn cash.
            #print(f"Total cash: ${player.you.money_in_hand}") 

        else:
            pass



### ------------------------------------------------------ ###


### Room Creation ###

# Kitchen #

kitchen_counter = Furniture("counter")
kitchen_counter.set_description("A white countertop with small black drops of paint deliberately splattered across it for decoration.\n"
                "You see a butter knife, a slice of cheese, and a metal pan.")
rm.kitchen.place_item(kitchen_counter)

fridge = Item("fridge")
fridge.set_description("You don't have time to eat right now.")
rm.kitchen.place_item(fridge)

sink = Furniture("sink")
sink.set_description("What, you need to wash your hands?  Get on with the game.")
rm.kitchen.place_item(sink)

butter_knife = Weapon("butter knife", 1)  # second argument is its damage.
butter_knife.set_description("A small, barely jagged knife.  Best used to spread condiments.")
rm.kitchen.place_item(butter_knife)

metal_pan = Weapon("metal pan", 5)
metal_pan.set_description("An old cast iron pan.  It's pretty heavy.  You could seriously whack somebody with this.")
rm.kitchen.place_item(metal_pan)

cheese = Item("cheese")
cheese.set_description("A single slice of yellow cheese.  I doubt this will come in handy.")
rm.kitchen.place_item(cheese)


# Dining hall #

dinner_table = Furniture("table")
dinner_table.set_description("A grayed, wooden table that can seat about 6 people.\n"
                "On one end, you see a box of matches and a yellow candle.")
rm.dining_hall.place_item(dinner_table)

candle = Item("candle")
candle.set_description("A half-melted candle on a brass candleholder.")
rm.dining_hall.place_item(candle)

matches = Item("matches")
matches.set_description("A small red and white box containing 4 matches.")
rm.dining_hall.place_item(matches)


# Dining hall to ballroom hallway

keys = Item("keys")
keys.set_description("Three keys held together by a rusty keyring.")
rm.dining_hall_to_ballroom_hallway.place_item(keys)


# Living room

couch = Furniture("couch", money_contained=1) # money_contained is solely for furniture items
couch.set_description("A dark gold hand-me-down that no longer provides any comfort, but you're way too poor to afford a replacement.  \n"
    "Home to many ants that have survived solely off old crumbs.")
rm.study.place_item(couch)

desk = Furniture("desk", money_contained=20)
desk.set_description("An oblong table you got at a thrift store years ago.\n"
    "All the junk on it has been rifled through, but nothing looks to be missing.\n"
    "A red key you've never seen before is among the mess.")
rm.study.place_item(desk)

red_key = Item("red key")
red_key.set_description("A tomato-colored house key.  Who knows what it opens.")
rm.study.place_item(red_key)


