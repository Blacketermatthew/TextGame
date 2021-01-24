#import item 

class Room():

    number_of_rooms = 0

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.items_in_room = {}
        Room.number_of_rooms = Room.number_of_rooms + 1

    def set_description(self, room_description):
        self.description = room_description

    # def get_description(self):
    #     return self.description

    def describe(self):
        print(self.description)

    # def set_name(self, room_name):
    #     self.name = room_name
    
    def get_name(self):
        return self.name

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def place_item(self, new_item):
        self.items_in_room[new_item.get_name()] = new_item

    def remove_item(self, name):
        self.items_in_room.pop(name, None)
        
    def get_all_items_in_room(self):
        return self.items_in_room

    def describe_item(self, name):
        return self.items_in_room[name].get_description()

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.name)
        print("-------------------")
        print(self.description, "\n")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name().lower() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            print(f"You go {direction}.")
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self


### ------------------------------------------------------ ###



### Room Creation ###

kitchen = Room("Kitchen")
kitchen.set_description("A small room with just enough space for a fridge and a sink.  The beige walls and yellow floor tile make you nauseous.\n"
    "Various items are scattered on the counter.")

dining_hall = Room("Dining hall")
dining_hall.set_description("Where we go to eat.  A table centers the room.  Atop the table are a candle and a few matches.")

living_room = Room("Living room")
living_room.set_description("Your safe space.  Your old, beat-up couch has seen better days. Haven't we all.\n"
    "It looks like all your stuff on your coffee table has been moved around or knocked over.")

dining_hall_to_ballroom_hallway = Room("Hallway")
dining_hall_to_ballroom_hallway.set_description("A short, narrow hallway.  At the end, two large doors.")

ballroom = Room("Ballroom")
ballroom.set_description("Despite the name, there are very few balls present.\n"
    "Light orange marble covers the circular dance floor, with white pillars standing along the outer edge.")


### Mapping Out the Rooms. ###

## link_room() connects one room to another room in the direction of wherever the parameter room is.  Room must first be declared as a Room() object
kitchen.link_room(dining_hall, "south") ## Makes the dining hall south of the kitchen, just as the next line places and connects it to the north

dining_hall.link_room(kitchen, "north")
dining_hall.link_room(dining_hall_to_ballroom_hallway, "west")
dining_hall.link_room(living_room, "east")

living_room.link_room(dining_hall, "west")

dining_hall_to_ballroom_hallway.link_room(dining_hall, "east")
dining_hall_to_ballroom_hallway.link_room(ballroom, "west")

ballroom.link_room(dining_hall_to_ballroom_hallway, "east")
