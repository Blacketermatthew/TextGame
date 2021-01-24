import pyfiglet  # This needs to be installed

class RPGInfo():
    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        #print("Welcome to " + self.title)
        welcome_banner = pyfiglet.figlet_format("GAME START")
        print("\n", "\n", welcome_banner)
        print("\nInstructions: Type north, south, east, or west to navigate.\n"
            "Use the commands available to interact with the world.\n\n"
            "Current objective: Explore.\n")




        