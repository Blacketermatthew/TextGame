from room import Room
from item import Item
from character import Character, Enemy

kitchen = Room("Kitchen")
kitchen.set_description("Your standard kitchen.  It's smaller than you'd like.")

ballroom = Room("Ballroom")
ballroom.set_description("Despite the name, there are very few balls present.  Light orange marble covers the circular floor, with white pillars standing along the outer edge.")

dining_hall = Room("Dining hall")
dining_hall.set_description("Where we go to eat.  A long, wooden table centers the room.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "east")
ballroom.link_room(dining_hall, "west")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

gorgo = Enemy("Gorgo", "A bulbous, gurgling bipedal creature with six bony arms.  Smells like trash.")
gorgo.set_weakness("flaming sword")
ballroom.set_character(gorgo)

current_room = kitchen
game = True

while game == True:
        print("\n")
        current_room.get_details()

        inhabitant = current_room.get_character()
        if inhabitant is not None:
                inhabitant.describe()

        command = (input("> ").lower())
        if command in ["north", "south", "east", "west"]:
                current_room = current_room.move(command)

        elif command == "talk":
                if inhabitant is not None:
                        talk_prompt = input("What would you like to say?: ")
                        print("[You say: " + talk_prompt + "]")
                elif inhabitant is None:
                         print("There is nobody here to talk to.")

        elif command == "fight":
                if inhabitant is not None:
                        fight_with = input("What will you fight with?: ")
                        fight_outcome = inhabitant.fight(fight_with)
                        if fight_outcome == True:
                                current_room.set_character(None)
                        elif fight_outcome == False:
                                print("You have been defeated.  GAME OVER")
                                game = False
                elif inhabitant is None:
                        print("There is nobody here to fight.")
                       

