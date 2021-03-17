from random import randint
import room as rm
from player import you

class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.previously_encountered = False
        self.insult_count = 0
        self.weakness = None

    # Describe this character
    def describe(self):
        if self.previously_encountered == True:
            print(f"\n{self.name} is here!")
        else: 
            print("\nA stranger is in here!")

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Defines its weakness 
    def set_weakness(self, weakness):
        self.weakness = weakness

    # Talk to this character
    def greet(self):
        if self.conversation is not None:
            if self.previously_encountered == True:
                print("[You greet " + self.name + ".]")
            else:
                self.previously_encountered = True
                print("[You greet the stranger.]")
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print("They just stare at you.")
    
    # Fight with this character
    def fight(self):
        self.previously_encountered = True

        if self.insult_count < 2:
            if isinstance(self, Character):
                print(self.name + " doesn't want to fight you.")
            else:
                pass

        elif self.insult_count >= 2 or isinstance(self, Enemy):
                you.check_inventory()
                combat_item = input("\n\nWhat will you fight with? : ")
                if combat_item == self.weakness:
                    if combat_item in you.inventory:
                        print("You fend " + self.name + " off with the " + combat_item)
                        return True
                    else:
                        print(f"You don't have that item in your inventory.  You were defenseless against {self.name}.")
                        return False
                else:
                    print(self.name + " crushes you like the nerd you are")
                    return False

    # Insult this character
    def insult(self):
        self.previously_encountered = True
        self.insult_count += 1
        if self.insult_count >=2:
            self.__class__ = Enemy
        
        insult_responses = { 
            0: "HEY.  Take it easy, pal.", 
            1: "Back off.  I'm warning you.", 
            2: "You're triggering me!!", 
            3: "You'll wish you never said that.",
            4: "C'mon.  Just leave me be!",
            5: "That's a really upsetting thing to hear.",
            6: "DUDE.",
            7: "That was uncalled for.",
            8: "Wow.",
            9: "As if I didn't already suffer from enough self-esteem issues."
            }

        print("[You insult " + self.name + "]")
        print("[" + self.name + " says]: " + insult_responses[randint(0,9)])   

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.insult_count = 2

    def get_weakness(self):
        return self.weakness
    
    def identify(self):
        self.previously_encountered = True
        print("[" + self.name + "]")
        print(self.description)
        print("[Weakness: " + self.weakness + "]")
    
### ------------------------------------------------------ ###


    
dave = Character("Dave", "A zombie with a terrible dairy allergy.")
dave.set_conversation("Brrlgrh... rgrhl... hello...")
dave.set_weakness("cheese")
rm.dining_hall.set_character(dave)

gorgo = Enemy("Gorgo", "A bulbous, gurgling bipedal creature with six bony arms.  Smells like trash.")
gorgo.set_weakness("flaming sword")
rm.garage.set_character(gorgo)
