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

    def type_text(self, text, delay=0.03):
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

        type_text("Welcome to...\n", 0.0125)

        print("""
        ████████████████████████████████████████████████████████████████████████████
        █░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
        █░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
        █░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
        █░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████
        █░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
        █░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
        █░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█
        █░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████████░░▄▀░░█░░▄▀░░█████████
        █░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█
        █░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
        █░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
        ████████████████████████████████████████████████████████████████████████████\n
        """)

        while True:
            begin_game = input("""
            Are you ready to begin playing the game?\n
            """)

            if begin_game.lower() == "yes" or "y":
                #Enter a try/except statement here at a later date
                self.type_text("Then let's begin...", 0.0125)
                self.play()
                break

            elif begin_game.lower() == "no" or "n":
                self.type_text("A wise choice...", 0.01)
                self.type_text("When you are ready, type 'y' and hit return")

            else:
                print(
                    f"{begin_game} is not a valid choice,
                    please enter 'y' or 'n' and try again."
                    )


    def restart(self):
        restart_prompt = input("""
        Would you like to play again? Y/N
        """).strip().lower()
        while True:
            if restart_prompt == "yes" or "y":
                current_node = start
                self.main_menu()
                break
            elif restart_prompt == "no" or "n":
                print("Thank you for playing!")
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
        while current_node:
            node = self.story_text[current_node]
            text = node["text"]
            options = node["options"]
            ending = node.get("ending")

            print(text)

            if ending == "1":
                self.type_text("""
                    Ending 1 of 4 has been discovered
                """)
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

            while options:
                choice = input("""
                What would you like to do? Enter 1 or 2 and then hit return
                """).strip()
                #Enter try/except statement later
                if choice != "1" or "2":
                    print("Please choose 1 or 2 and hit return")
                else:
                    current_node = options[f"option_{choice}"]
                    break

if __name__ == "__main__":
    game = House()
    game.main_menu()
