import pyfiglet  # This needs to be installed
from pyfiglet import fonts

class RPGInfo():
    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        welcome_banner = "GAME START"
        #welcome_banner = pyfiglet.figlet_format("GAME START")
        print("\n\n", welcome_banner)
        print("\nInstructions: Type north, south, east, or west to navigate.\n"
            "Use the commands available to interact with the world.\n\n"
            "Objective: Try and find all three keys!\n")




        