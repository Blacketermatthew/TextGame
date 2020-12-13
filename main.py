from room import Room
from item import Item
from character import Character, Enemy
from rpginfo import RPGInfo

#### ------- TO DO LIST -------------- ####
"""
- Create items.  
- Create figure out how to add items to rooms
- Create an inventory or backpack system
- Create stats for characters and items
- Maybe? Have identify distinguish between characters and items 
        (i.e. "identify stranger" vs "identify sword")
- Have stats work almost like skill rolls when trying to identify, fight, etc
- Maybe? Allow for clothing and armor
-
 
 
"""
#### --------------------------------- ####

main_game = RPGInfo("Untitled Game")
main_game.welcome()

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
dead = False

while dead == False:
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
                        inhabitant.previously_encountered = True
                        talk_prompt = input("What would you like to say? : ")
                        print("\n[You say: " + talk_prompt + "]")
                        print("[" + inhabitant.name + " says]: " + inhabitant.conversation)
                elif inhabitant is None:
                         print("There is nobody here to talk to.")

        elif command == "fight":
                if inhabitant is not None and isinstance(inhabitant, Enemy):
                        fight_with = input("What will you fight with? : ")
                        fight_outcome = inhabitant.fight(fight_with)
                        if fight_outcome == True:
                                current_room.set_character(None)
                        elif fight_outcome == False:
                                print("You have been defeated.  GAME OVER")
                                dead = True
                elif inhabitant is not None and isinstance(inhabitant, Character):
                        print("You should not fight someone who isn't your enemy!")
                elif inhabitant is None:
                        print("There is nobody here to fight.")
                else:
                        print("You are currently unable to fight anybody.")
                       
        elif command == "identify":
                if inhabitant is not None:
                        inhabitant.identify()
                elif inhabitant is None:
                        print("There is nobody here to identify.")

        elif command == "insult":
                if inhabitant is not None:
                        inhabitant.insult()
                elif inhabitant is None:
                        print("There is nobody here to insult.")

