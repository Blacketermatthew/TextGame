from item import *

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

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def set_name(self, room_name):
        self.name = room_name
    
    def get_name(self):
        return self.name

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    # def set_item(self, new_item):
    #     self.item = new_item

    def place_item(self, new_item):
        self.items_in_room[new_item.get_name()] = new_item

    def remove_item(self, name):
        self.items_in_room.pop(name, None)
        #return self.items_in_room

    def get_all_items_in_room(self):
        return self.items_in_room

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.name)
        print("-------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("\nYou can't go that way")
            return self