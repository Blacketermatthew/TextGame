#import player
from player import you
import room as rm
from item import Item, Furniture, Weapon
#import character as char
from character import Character, Enemy
from rpginfo import RPGInfo

## ------- TO DO LIST -------------- ##
"""
- Create stats for characters and items
- Have stats work almost like skill rolls when trying to identify, fight, etc


"""
## --------------------------------- ##



### Room Creation ###

### Mapping Out the Rooms. ###

### Creating the Characters and Enemies ###

### Creating and Placing Items ###



###############################################################
################### MAIN GAME #################################
###############################################################

### Game Variable Setup ###
current_room = rm.study  ## Where you start off.
#player = Player()
inventory = you.inventory  # This is an empty list in Item that will have taken items appended to, so it follows them between rooms.

dead = False  ## Gets turned True once you die
main_game = RPGInfo("Untitled Game")  ## Creates an instance of the title screen
main_game.welcome()  



### Main Game/Command Loop ###
# This baby keeps the game going while you're alive.
while dead == False:
        print("\n===============================================================================\n\n")
        
        current_room.get_details()
        inhabitant = current_room.get_character()
        items_in_room = current_room.get_all_items_in_room()

<<<<<<< HEAD
<<<<<<< HEAD
                if inhabitant is not None:
<<<<<<< HEAD
                        inhabitant.describe()
=======
<<<<<<< HEAD
                        inhabitant.greet()
                elif inhabitant is None:
                        print("There is nobody here to talk to.")

        elif command == "fight":

                if inhabitant is not None and isinstance(inhabitant, Enemy):
                        you.check_inventory()
                        fight_with = input("\n\nWhat will you fight with? : ")
                        fight_outcome = inhabitant.fight(fight_with)
                        if fight_outcome == True:
                                current_room.set_character(None)
                        elif fight_outcome == False:
                                print("\nYou have been defeated.  GAME OVER")
                                dead = True
=======
                        inhabitant.describe()
>>>>>>> 3d331e8a80de676cf544c72e1f338621156f5ec1
>>>>>>> 4f2bc797305e7db984bcec48866bd51f79be5c21

                print("\n\nCommands available: [ Greet | Insult | Identify | Fight | Look At ___ | Take ___ | Inventory ]")
                command = (input("> ").lower().rstrip())
                print("\n\n\n\n===============================================================================\n")
<<<<<<< HEAD

=======
        if inhabitant is not None:
                inhabitant.describe()

        print("\n\nCommands available: [ Greet | Insult | Identify | Fight | Look At ___ | Take ___ | Inventory ]")
        command = (input("> ").lower().rstrip())
        print("\n\n\n\n===============================================================================\n")
>>>>>>> parent of 3d331e8 (Added win condition for keys)
=======
        if inhabitant is not None:
                inhabitant.describe()

        print("\n\nCommands available: [ Greet | Insult | Identify | Fight | Look At ___ | Take ___ | Inventory ]")
        command = (input("> ").lower().rstrip())
        print("\n\n\n\n===============================================================================\n")
>>>>>>> parent of 3d331e8 (Added win condition for keys)

=======

<<<<<<< HEAD
<<<<<<< HEAD

>>>>>>> 4f2bc797305e7db984bcec48866bd51f79be5c21
                if command in ["north", "south", "east", "west"]:
=======
        if command in ["north", "south", "east", "west"]:
>>>>>>> parent of 3d331e8 (Added win condition for keys)

                current_room = current_room.move(command)

<<<<<<< HEAD
<<<<<<< HEAD
                elif command == "greet": 
=======
        if command in ["north", "south", "east", "west"]:

                current_room = current_room.move(command)

        elif command == "greet": 
>>>>>>> parent of 3d331e8 (Added win condition for keys)

                if inhabitant is not None:
                        inhabitant.greet()
                elif inhabitant is None:
                        print("There is nobody here to talk to.")

        elif command == "fight":

                if inhabitant is not None and isinstance(inhabitant, Enemy):
                        you.check_inventory()
                        fight_with = input("\n\nWhat will you fight with? : ")
                        fight_outcome = inhabitant.fight(fight_with)
                        if fight_outcome == True:
                                current_room.set_character(None)
                        elif fight_outcome == False:
                                print("\nYou have been defeated.  GAME OVER")
                                dead = True

                elif inhabitant is not None and isinstance(inhabitant, Character):
                        inhabitant.fight(None)

                elif inhabitant is None:
                        print("There is nobody here to fight.")

                else:
                        print("You are currently unable to fight anybody.")
                
        elif command == "identify":

<<<<<<< HEAD
                        if inhabitant is not None and isinstance(inhabitant, Enemy):
=======
<<<<<<< HEAD
                # If you insult somebody 3+ times, they'll attack you.  Insulting an enemy once will cause them to immediately attack you.
                if inhabitant is not None:
                        if inhabitant.__class__.__name__ == "Enemy": 
                                inhabitant.insult_count = 2   

                        if inhabitant.insult_count >= 2:
                                you.check_inventory()
                                print(f"\n\n{inhabitant.name}, now angry, is charging towards you.")
=======
                elif command == "greet": 
=======
        elif command == "greet": 
>>>>>>> parent of 3d331e8 (Added win condition for keys)

                if inhabitant is not None:
                        inhabitant.greet()
                elif inhabitant is None:
                        print("There is nobody here to talk to.")

        elif command == "fight":

                if inhabitant is not None and isinstance(inhabitant, Enemy):
                        you.check_inventory()
                        fight_with = input("\n\nWhat will you fight with? : ")
                        fight_outcome = inhabitant.fight(fight_with)
                        if fight_outcome == True:
                                current_room.set_character(None)
                        elif fight_outcome == False:
                                print("\nYou have been defeated.  GAME OVER")
                                dead = True

                elif inhabitant is not None and isinstance(inhabitant, Character):
                        inhabitant.fight(None)

                elif inhabitant is None:
                        print("There is nobody here to fight.")

                else:
                        print("You are currently unable to fight anybody.")
                
        elif command == "identify":

<<<<<<< HEAD
                        if inhabitant is not None and isinstance(inhabitant, Enemy):
>>>>>>> 3d331e8a80de676cf544c72e1f338621156f5ec1
>>>>>>> 4f2bc797305e7db984bcec48866bd51f79be5c21
=======
=======
>>>>>>> parent of 3d331e8 (Added win condition for keys)
                if inhabitant is not None:
                        if inhabitant.__class__.__name__ == "Enemy":
                                inhabitant.identify()
                        else:
                                print(f"You are unable to get a read on {inhabitant.name}")                
                                        
                elif inhabitant is None:
                        print("There is nobody here to identify.")

        elif command == "insult":

                # If you insult somebody 3+ times, they'll attack you.  Insulting an enemy once will cause them to immediately attack you.
                if inhabitant is not None:
                        if inhabitant.__class__.__name__ == "Enemy": 
                                inhabitant.insult_count = 2   

                        if inhabitant.insult_count >= 2:
                                you.check_inventory()
                                print(f"\n\n{inhabitant.name}, now angry, is charging towards you.")
<<<<<<< HEAD
>>>>>>> parent of 3d331e8 (Added win condition for keys)
=======
>>>>>>> parent of 3d331e8 (Added win condition for keys)
                                fight_with = input("What will you fight with? : ")
                                fight_outcome = inhabitant.fight(fight_with)
                                if fight_outcome == True:
                                        current_room.set_character(None)
                                elif fight_outcome == False:
                                        print("\nYou have been defeated.  GAME OVER")
                                        dead = True
<<<<<<< HEAD
<<<<<<< HEAD
                        else:
                                inhabitant.insult()  

                        elif inhabitant is not None and isinstance(inhabitant, Character):
                                inhabitant.fight(None)
<<<<<<< HEAD

                        elif inhabitant is None:
                                print("There is nobody here to fight.")

=======

                        elif inhabitant is None:
                                print("There is nobody here to fight.")

>>>>>>> 4f2bc797305e7db984bcec48866bd51f79be5c21
=======
>>>>>>> parent of 3d331e8 (Added win condition for keys)
                        else:
                                inhabitant.insult()  

                elif inhabitant is None:
                        print("There is nobody here to insult.")

        elif command == "inventory":

                you.check_inventory()

        elif command.startswith("take") is True:

=======
                        else:
                                inhabitant.insult()  

                elif inhabitant is None:
                        print("There is nobody here to insult.")

        elif command == "inventory":

                you.check_inventory()

        elif command.startswith("take") is True:

>>>>>>> parent of 3d331e8 (Added win condition for keys)
                if items_in_room is not None:
                        item_taken = command[5:]  # This grabs the text after "take " to check l
                        if item_taken in items_in_room:
                                if items_in_room[item_taken].can_put_in_inventory == True:
                                        print(f"You add {item_taken} to your inventory.") 
                                        inventory[item_taken] = items_in_room[item_taken]  #  Adds item to inventory
                                        current_room.remove_item(item_taken)
                                        #items_in_room.pop(item_taken)  # Removes item from that room's dict.
                                else:
                                        print("You are unable to add that item to your inventory.")

                        elif item_taken in inventory:
                                print("You've already added that to your inventory.")
                        else:
                                 print(f"I'm not sure that I see '{item_taken}' in here.  What would you like to take?")

                elif items_in_room is None:
                        print("There is nothing in the room to take")

        elif command.startswith("look at") is True:

                object_looked_at = command[8:]  # Everything after "look at " is grabbed

                # Items are placed in different dicts depending on if they're in your inentory or still in the room.
                # This if else statement prints the descriptions for these items.
                if object_looked_at in items_in_room:
                        current_room.describe_item(object_looked_at)
                        
                        if items_in_room[object_looked_at].__class__.__name__ == "Furniture":
                                cash_found = items_in_room[object_looked_at].money_contained 
                                if cash_found > 0:
                                        items_in_room[object_looked_at].take_money()

                elif object_looked_at in inventory:
                        inventory[object_looked_at].get_description()
                        
                else:
                        print(f"I'm not sure that I see '{object_looked_at}'.  What would you like to look at?")

        else: 
                print(f"Sorry, I did not understand the command: '{command}'")

