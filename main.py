from player import you
import room as rm
from item import Item, Furniture, Weapon, red_key, blue_key, yellow_key
from character import Character, Enemy
from rpginfo import RPGInfo


###############################################################
################### MAIN GAME #################################
###############################################################

### Game Variable Setup ###
current_room = rm.study  ## Where you start off.
inventory = you.inventory  # This is an empty list in Item that will have taken items appended to, so it follows them between rooms.

dead = False  ## Gets turned True once you die
main_game = RPGInfo("Untitled Game")  ## Creates an instance of the title screen
main_game.welcome()  



### Main Game/Command Loop ###
# This baby keeps the game going while you're alive.
while dead == False:
        
        # Win condition.  Once you've collected all the keys, it will stop the game.  Very retro, I know, but I'm just one man trying to make a tiny game demo!
        if all(key in inventory for key in ("red key", "blue key", "yellow key")):  
                print("\n\nYou've collected all three keys.")
                print("You win!")
                break
        
        else:
                print("\n===============================================================================\n\n")
                
                current_room.get_details()
                inhabitant = current_room.get_character()
                items_in_room = current_room.get_all_items_in_room()

                if inhabitant is not None:
                        inhabitant.describe()

                print("\n\nCommands available: [ Greet | Insult | Identify | Fight | Look At ___ | Take ___ | Inventory ]")
                command = (input("> ").lower().rstrip())
                print("\n\n\n\n===============================================================================\n")


                if command in ["north", "south", "east", "west"]:

                        current_room = current_room.move(command)

                elif command == "greet": 

                        if inhabitant is not None:
                                inhabitant.greet()
                        elif inhabitant is None:
                                print("There is nobody here to talk to.")

                elif command == "fight":

                        if inhabitant is not None and isinstance(inhabitant, Enemy):
                                fight_outcome = inhabitant.fight()
                                if fight_outcome == True:
                                        current_room.set_character(None)
                                elif fight_outcome == False:
                                        print("\nYou have been defeated.  GAME OVER")
                                        dead = True

                        elif inhabitant is not None and isinstance(inhabitant, Character):
                                inhabitant.fight()

                        elif inhabitant is None:
                                print("There is nobody here to fight.")
                        
                elif command == "identify":

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
                                
                                if inhabitant.insult_count < 2 and isinstance(inhabitant, Character):
                                        inhabitant.insult()   

                                elif inhabitant.insult_count > 2 or isinstance(inhabitant, Enemy):
                                        print(inhabitant.name + ", now angry, is charging towards you.\n")
                                        fight_outcome = inhabitant.fight()
                                        if fight_outcome == True:
                                                current_room.set_character(None)
                                        elif fight_outcome == False:
                                                print("\nYou have been defeated.  GAME OVER")
                                                dead = True

                        elif inhabitant is None:
                                print("There is nobody here to insult.")

                elif command == "inventory":

                        you.check_inventory()

                elif command.startswith("take") is True:

                        if items_in_room is not None:
                                item_taken = command[5:]  # This grabs the text after "take " to check l
                                if item_taken in items_in_room:
                                        if items_in_room[item_taken].can_put_in_inventory == True:
                                                print(f"You add {item_taken} to your inventory.") 
                                                inventory[item_taken] = items_in_room[item_taken]  #  Adds item to inventory
                                                current_room.remove_item(item_taken)
                                                
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
        
