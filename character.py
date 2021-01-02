from random import randint

class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.previously_encountered = False
        self.insult_count = 0
        #self.weakness = None

    # Describe this character
    def describe(self):
        if self.previously_encountered == True:
            print(self.name + " is here!")
        else: 
            print("A stranger is in here!")

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_weakness(self, weakness):
        self.weakness = weakness

    # Talk to this character
    def greet(self):
        if self.conversation is not None:
            self.previously_encountered = True
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " just stares at you.")
    
    # Fight with this character:
    def fight(self, combat_item):
        self.previously_encountered = True
        if self.insult_count >= 3:
            if combat_item == self.weakness:
                print("You fend " + self.name + " off with the " + combat_item)
                return True
            else:
                print(self.name + " crushes you like the nerd you are")
                return False
        else:
            print(self.name + " doesn't want to fight you.")
        
    # Insult this character
    def insult(self):
        self.previously_encountered = True
        #self.insult_count += 1
        insult_responses = { 
            0: "HEY.  Take it easy, pal.", 
            1: "Back off.  I'm warning you.", 
            2: "You're triggering me!!", 
            3: "You'll wish you never said that.",
            4: "C'mon, dude.  Just leave me be.",
            5: "That's a really upsetting this to hear.",
            6: "DUDE."
            }

        print("[You insult " + self.name + "]")
        print("[" + self.name + " says]: " + insult_responses[randint(0,6)])   

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def get_weakness(self):
        return self.weakness
    
    def identify(self):
        self.previously_encountered = True
        print("[" + self.name + "]")
        print(self.description)
        print("[Weakness: " + self.weakness + "]")

    def fight(self, combat_item):
        self.previously_encountered = True
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you like the nerd you are")
            return False
    