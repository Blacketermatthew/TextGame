import pyfiglet  # This needs to be installed

class RPGInfo():
    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        #print("Welcome to " + self.title)
        welcome_banner = pyfiglet.figlet_format("WELCOME")
        print("\n", "\n", welcome_banner)
        print("\nInstructions: Type north, south, east, or west to navigate.  \
            \nUse the commands available to interact with the world.")




        