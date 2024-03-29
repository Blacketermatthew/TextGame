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

    def describe(self):
        print(self.description)
    
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

dining_hall = Room("Dining hall")
dining_hall.set_description("Where we go to eat.  A table centers the room.  Atop the table are a candle and a few matches.")

kitchen = Room("Kitchen")
kitchen.set_description("A small room with just enough space for a fridge and a sink.  The beige walls and yellow floor tile make you nauseous.\n"
    "Various items are scattered on the counter.")

foyer = Room("Foyer")
foyer.set_description("A room whose presence alone just screams \"upper class.\"  Mainly used for hanging stuff on the key hooks and coat rack in there.")

study = Room("Study")
study.set_description("Your safe space.  The old, beat-up couch in here has seen better days. Haven't we all.\n"
    "It looks like all your stuff on your desk has been moved around or knocked over.")

bedroom = Room("Bedroom")
bedroom.set_description("Where insomnia crushes any dreams you have of getting sleep.  The trunk at the foot of your bed has... steam? coming out of it.")

upstairs_hallway = Room("Upstairs hallway")
upstairs_hallway.set_description("A small hallway with white walls and a surprisingly high amount of warm, natural light coming from downstairs.\n"
    "A cat's paradise, they'd say.  There's an old framed poster that's fallen off the wall and onto the floor.")

dining_hall_to_garage_hallway = Room("Hallway")
dining_hall_to_garage_hallway.set_description("A short, narrow hallway.  At the end, two large doors.")

garage = Room("Garage")
garage.set_description("Mostly used for storage.  If you pushed all the random junk to one side of the room, you could MAYBE fit a small sedan in here.\n"
    "The only clean area in here is your pride and joy, your workbench.")


### Mapping Out the Rooms. ###

## link_room() connects one room to another room in the direction of wherever the parameter room is.  Room must first be declared as a Room() object

dining_hall.link_room(kitchen, "north")  ## Makes the dining hall south of the kitchen, just as the next line places and connects it to the north
dining_hall.link_room(foyer, "south")
dining_hall.link_room(dining_hall_to_garage_hallway, "west")
dining_hall.link_room(study, "east")

kitchen.link_room(dining_hall, "south")

study.link_room(dining_hall, "west")

foyer.link_room(dining_hall, "north")
foyer.link_room(upstairs_hallway, "east")

upstairs_hallway.link_room(foyer, "west")
upstairs_hallway.link_room(bedroom, "east")

bedroom.link_room(upstairs_hallway, "west")

dining_hall_to_garage_hallway.link_room(dining_hall, "east")
dining_hall_to_garage_hallway.link_room(garage, "west")

garage.link_room(dining_hall_to_garage_hallway, "east")
