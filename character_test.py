from item import Item, Weapon
from character import Character
from character import Enemy
dave = Character("Dave", "A good man")

#dave.set_conversation("Hey there!  Dave's the name.  What can I do for you?")
#dave.talk()
#dave.insult()

gorgo = Enemy("Gorgo", "A bulbous, gurgling bipedal creature with six bony arms.  Smells like trash.")
gorgo.set_weakness("flaming sword")
        
#fight_with = input()
#gorgo.fight(fight_with)

dave = Character("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")

#print(dave.__class__.__name__)

# sample_input = (input("What is your next command?: ").lower())
# print(sample_input.startswith("hello"))
# print(sample_input)

inventory = Item.inventory 
print(inventory)