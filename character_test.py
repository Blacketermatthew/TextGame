from character import Character
from character import Enemy
dave = Character("Dave", "A good man")

#dave.set_conversation("Hey there!  Dave's the name.  What can I do for you?")
#dave.talk()
#dave.insult()

gorgo = Enemy("Gorgo", "A bulbous, gurgling bipedal creature with six bony arms.  Smells like trash.")
gorgo.set_weakness("flaming sword")
gorgo.talk()
print("What will you fight with?")
fight_with = input()
gorgo.fight(fight_with)

