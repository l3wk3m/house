import sys
import time

from story import story_text

"""
Welcome the player to the game.
Tell them this is a survival horror text based adventure game.
Ask them if they'd like to try escape...HOUSE (in ascii art)
y/n/how to play
"""


class Player:
    """
    This is the class of Player that will hold a value
    that will be used to evaluate whether or not the Player
    is holding the key needed for the game's true ending.
    """
    def __init__(self, has_key):
        self.has_key = has_key

    def take_key(self):
        self.has_key = True


class House:
    """
    This is the main class for the game 'House'
    This is the sttucture I will be using to call
    and evaluate player choices from the dicts
    in the story.py file
    """
    def __init__(self):
        """
        This is the initialiser for the game.
        It launches an instance of House to the virtual terminal
        and calls the dict in story.py to prompt the user with
        choices from which they will play out the text-based
        adventure.
        """
        self.story_text = story_text

    def type_text(self, text, delay=0.01):
        """
        Simulates the printing speed of a terminal to give the
        Player a feeling that they're experiencing the story
        as it is happening to them.
        A default typespeed is passed but this can be altered
        for more dramatic moments in the game.

        Credit for this code to github.com/queenisabaer
        and github.com/gayatrig19
        """

        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def main_menu(self):
        """
        Displays the game title to the terminal in ASCII
        characters and prompts the player if they would like
        to begin the game.
        """

        self.type_text("Welcome to...\n", 0.06)

        print("""
        
────────────────────────────────────────────────────────────────────────────
─██████──██████─██████████████─██████──██████─██████████████─██████████████─
─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██──██░░██─██░░██████░░██─██░░██──██░░██─██░░██████████─██░░██████████─
─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██░░██─────────██░░██─────────
─██░░██████░░██─██░░██──██░░██─██░░██──██░░██─██░░██████████─██░░██████████─
─██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████░░██─██░░██──██░░██─██░░██──██░░██─██████████░░██─██░░██████████─
─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─────────██░░██─██░░██─────────
─██░░██──██░░██─██░░██████░░██─██░░██████░░██─██████████░░██─██░░██████████─
─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████──██████─██████████████─██████████████─██████████████─██████████████─
────────────────────────────────────────────────────────────────────────────\n
        """)

        while True:
            begin_game = input("""
            Are you ready to begin playing the game?\n
            """).lower()
            try:
                if begin_game == "yes" or begin_game == "y":
                    #Enter a try/except statement here at a later date
                    self.type_text("Then let's begin...", 0.01)
                    self.play()
                    break

                elif begin_game == "no" or begin_game == "n":
                    self.type_text("A wise choice...\n", 0.01)
                    self.type_text("When you are ready, type 'y' and hit return")
                    print(begin_game)

                else:
                    if begin_game.isalpha() == False:
                        raise ValueError
                    print(f"""
                    {begin_game} is not a valid choice.
                    Please enter 'y' or 'n' and try again."
                    """)

            except ValueError as e:
                print(f"""
                {begin_game} raised a ValueError : {e}
                Please enter 'y' or 'n' and try again."
                    """)


    def restart(self):
        while True:
            restart_prompt = input("""
        Would you like to play again?
        """).strip().lower()
            if restart_prompt == "no" or restart_prompt == "n":
                print("Thank you for playing!")
                break
            elif restart_prompt == "yes" or restart_prompt == "y":
                current_node = "start"
                self.main_menu()
                break
            else:
                print("Invalid input. Please type 'Y' or 'N' and hit return")


    def play(self, current_node="start"):
        """
        The main function of run.py
        This will iterate through every other function in the file
        to execute the game loop.
        This displays the start screen, gives the option of
        displaying game instructions, the option of starting the
        game and then executes the game loop, pulling player
        options from the dictionary in story.py.
        """
        player_char = Player(False)

        while current_node:
            node = self.story_text[current_node]
            text = node["text"]
            options = node["options"]
            ending = node.get("ending")
            key = node.get("key")

            print(text)

            if ending == "1":
                self.type_text("""
                    Ending 1 of 4 has been discovered
                """, 0)
                self.restart()
                break
            elif ending == "2":
                self.type_text("""
                Ending 2
                """)
                self.restart()
                break
            elif ending == "3":
                self.type_text("""
                Ending 3
                """)
                self.restart()
                break
            elif ending == "4":
                self.type_text("""
                Ending 4
                """)
                self.restart()
                break

            if key == "acquired":
                player_char.take_key()
                print("You've acquired a key - this could come in handy later...")

            if options:
                choice = input("""
                What would you like to do? Enter 1 or 2 and then hit return
                """).strip()
                #Enter try/except statement later
                while choice not in ["1", "2"]:
                    print("Please choose 1 or 2 and hit return")
                current_node = options[f"option_{choice}"]
            else:
                current_node = None

            print("Thank you for playering ERROR")

if __name__ == "__main__":
    game = House()
    game.main_menu()
