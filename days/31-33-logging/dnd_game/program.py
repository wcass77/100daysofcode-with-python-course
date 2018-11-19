"""
List of potential error states:
Invalid parameter for creature creation
The user enters something invalid: The program should recover, list options
The program should also respond correctly if you type out command
Keyboard interrupt: Program should exit gracefully
Life is less than 0: Should tell you that you're dead and exit
"""
import random

import logbook

from actors import Creature, Dragon, Wizard


def main():
    logbook.TimedRotatingFileHandler("rpg_log", level=logbook.TRACE).push_application()
    app_logger = logbook.Logger("App")
    try:
        app_logger.trace("Setting up game ...")
        game = Game()
        app_logger.trace("Game setup finished")
    except Exception as e:
        print(f"There was an error setting up the game: {e}")
        app_logger.error("There was an error setting up the game:")
        app_logger.exception(e)
        return
    game.print_header()
    try:
        app_logger.trace("Entering Game Loop")
        game.loop()
        app_logger.trace("Exited game loop normally")
    except KeyboardInterrupt as e:
        print(f"\nKeyboard Interrupt: Quitting the game...")
        app_logger.warn("Keyboard Interrupt: Quitting the game...")
    except Exception as e:
        print(f"Exception during the game:{e}")
        app_logger.error("Uncaught exception, exiting the game")
        app_logger.exception(e)


class Game:
    log = logbook.Logger("Game Log")

    def __init__(self):
        self._setup_creatures()
        self._setup_hero()

    def _setup_creatures(self):
        self.log.trace("Setting up creatures")
        try:
            self.creatures = [
                Creature("Bat", 5),
                Creature("Toad", 1),
                Creature("Tiger", 12),
                Dragon("Black Dragon", 50, scaliness=2, breaths_fire=False),
                Wizard("Evil wizard", 1000),
            ]
        except TypeError as e:
            print(f"There was a problem creating the creatures")
            self.log.error("Problem setting up creatures!")
            raise e

    def _setup_hero(self):
        self.log.trace("Setting up Hero")
        try:
            self.hero = Wizard("Gandolf", 75)
        except TypeError as e:
            print(f"There was a problem creating the hero")
            self.log.error("Problem setting up hero!")
            raise e

    @staticmethod
    def print_header():
        print("---------------------------------")
        print("          WIZARD GAME")
        print("---------------------------------")
        print()

    def handle_command(self, cmd):
        if cmd == "a":
            self.log.trace(f"Hero attacks! {self.active_creature.name}")
            if self.hero.attack(self.active_creature):
                print("The wizard defeated {}".format(self.active_creature.name))
                self.log.trace(f"Hero wins!")
                self.creatures.remove(self.active_creature)
            else:
                print(
                    "The wizard has been defeated by the powerful {}".format(
                        self.active_creature.name
                    )
                )
                self.log.trace("Hero loses!")
        elif cmd == "r":
            print("The wizard has become unsure of his power and flees!!!")
            self.log.trace(f"Hero runs from {self.active_creature.name}")
        elif cmd == "l":
            self.log.trace(f"The wizard looks around")
            print(
                "The wizard {} takes in the surroundings and sees:".format(
                    self.hero.name
                )
            )
            for c in self.creatures:
                print(" * {} of level {}".format(c.name, c.level))
        else:
            self.log.warn(f"Invalid keyboard entry by user: {cmd}")
            raise ValueError(cmd)

    def loop(self):

        while True:

            self.active_creature = random.choice(self.creatures)
            self.log.trace(f"New opponent appears: {self.active_creature.name}")
            print(
                "A {} of level {} has appear from a dark and foggy forest...".format(
                    self.active_creature.name, self.active_creature.level
                )
            )
            print()
            while True:
                try:
                    self.handle_command(
                        input("Do you [a]ttack, [r]unaway, or [l]ook around? ")
                    )
                    break
                except ValueError as e:
                    print(f"Invalid command {e}. Try again")
            if not self.creatures:
                print("You've defeated all the creatures, well done!")
                self.log.trace("Hero wins!")
                break

            print()


if __name__ == "__main__":
    main()
