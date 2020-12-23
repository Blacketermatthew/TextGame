from room import Room
from item import Item, Weapon
from character import Character, Enemy
from rpginfo import RPGInfo

## ------- TO DO LIST -------------- ##
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
## --------------------------------- ##



### Room Creation ###
kitchen = Room("Kitchen")
kitchen.set_description("Your standard kitchen.  It's smaller than you'd like.")

dining_hall = Room("Dining hall")
dining_hall.set_description("Where we go to eat.  A table centers the room.  Atop the table is a candle and a few matches.")

dining_hall_to_ballroom_hallway = Room("Hallway")
dining_hall_to_ballroom_hallway.set_description("A short, narrow hallway.  At the end, two large doors.")

ballroom = Room("Ballroom")
ballroom.set_description("Despite the name, there are very few balls present.  Light orange marble covers the circular dance floor, with white pillars standing along the outer edge.")


### Mapping Out the Rooms. ###
## link_room() connects one room to another room in the direction of wherever the parameter room is.  Room must first be declared as a Room() object
kitchen.link_room(dining_hall, "south") ## Makes the dining hall south of the kitchen, just as the next line places and connects it to the north
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(dining_hall_to_ballroom_hallway, "west")
dining_hall_to_ballroom_hallway.link_room(dining_hall, "east")
dining_hall_to_ballroom_hallway.link_room(ballroom, "west")
ballroom.link_room(dining_hall_to_ballroom_hallway, "east")


### Creating the Characters and Enemies ###
dave = Character("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

gorgo = Enemy("Gorgo", "A bulbous, gurgling bipedal creature with six bony arms.  Smells like trash.")
gorgo.set_weakness("flaming sword")
ballroom.set_character(gorgo)


### Creating and Placing Items ###






######################################################
################### MAIN GAME ########################
######################################################

### Game Setup ###
current_room = kitchen  ## Where you start off.
dead = False  ## Gets turned True once you die

main_game = RPGInfo("Untitled Game")  ## Creates an instance of the title screen
main_game.welcome()  

while dead == False:
        print("\n")
        current_room.get_details()

        inhabitant = current_room.get_character()
        if inhabitant is not None:
                inhabitant.describe()

        print("\nCommands available : [ Greet | Insult | Identify | Fight ]")
        command = (input("> ").lower())
        print("\n")
        if command in ["north", "south", "east", "west"]:
                current_room = current_room.move(command)

        elif command == "greet": 
                if inhabitant is not None:
                        inhabitant.previously_encountered = True
                        print("\n[You greet " + inhabitant.name + "]")
                        inhabitant.greet()
                elif inhabitant is None:
                         print("\nThere is nobody here to talk to.")

        elif command == "fight":
                if inhabitant is not None and isinstance(inhabitant, Enemy):
                        fight_with = input("What will you fight with? : ")
                        fight_outcome = inhabitant.fight(fight_with)
                        if fight_outcome == True:
                                current_room.set_character(None)
                        elif fight_outcome == False:
                                print("\nYou have been defeated.  GAME OVER")
                                dead = True
                elif inhabitant is not None and isinstance(inhabitant, Character):
                        print("\nYou should not fight someone who isn't your enemy!")
                elif inhabitant is None:
                        print("\nThere is nobody here to fight.")
                else:
                        print("\nYou are currently unable to fight anybody.")
                       
        elif command == "identify":
                if inhabitant is not None:
                        inhabitant.identify()
                elif inhabitant is None:
                        print("\nThere is nobody here to identify.")

        elif command == "insult":
                if inhabitant is not None:
                        if inhabitant.insult_count < 3:
                                inhabitant.insult()             
                        elif inhabitant.insult_count >= 3:
                                print(inhabitant.name + ", now angry, is charging towards you.")
                                fight_with = input("What will you fight with? : ")
                                fight_outcome = inhabitant.fight(fight_with)
                                if fight_outcome == True:
                                        current_room.set_character(None)
                                elif fight_outcome == False:
                                        print("\nYou have been defeated.  GAME OVER")
                                        dead = True
                elif inhabitant is None:
                        print("\nThere is nobody here to insult.")

