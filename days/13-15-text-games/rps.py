from art import tprint
import random

ROUNDS = 3  # The number of rounds of RPS to be played
ROLLS = [
    "rock",
    "paper",
    "sissors",
]  # order such that each beats the previous item in list
WIN = 2
LOSE = 0
DRAW = 1


class Roll:
    """Class that holds a particular roll and knows the rules"""

    def __init__(self, rps="random"):
        if rps in ROLLS:
            self.name = rps
        elif rps == "random":
            self.name = random.choice(ROLLS)

    def against(self, your_roll):
        """Returns WIN if I win, LOSE if I lose, and DRAW for a tie.
        Relies on ROLLS being in order such that each item beats the next item.
        Returns a tuple with the first value being for my role and the second
        being for your role"""
        if self.name == your_roll.name:
            return (DRAW, DRAW)
        my_roll_num = ROLLS.index(self.name)
        your_roll_num = ROLLS.index(your_roll.name)
        if (my_roll_num - 1) % len(ROLLS) == your_roll_num:
            return (WIN, LOSE)
        return (LOSE, WIN)


class Player:
    def __init__(self, name, cpu=False):
        self.name = name
        self.record = []  # list of outcomes as ints
        self.rolls = []  # list of rolls
        self.cpu = cpu

    def roll(self, roll=None):
        """add a new roll to player"""
        if self.cpu:
            self.rolls.append(Roll())
        elif roll in ROLLS:
            self.rolls.append(Roll(roll))
        else:
            raise Exception("Invalid role chosen")

    def new_result(self, result):
        self.record.append(result)


def get_user_roll():
    roll = input(
        f"What do you roll? Type full word or first letter. Possible values: {ROLLS}"
    )
    if roll in ROLLS:
        return roll
    if len(roll) == 1:
        for possible_role in ROLLS:
            if roll == possible_role[0]:
                return possible_role
    print("Please enter a valid roll")
    return get_user_roll()


def main():
    tprint("Rock\nPaper\nSissors", font="Epic")
    name = input("What is your name?:")
    tprint(f"Welcome   {name}!", font="Doom")
    player = Player(name)
    cpu = Player("Computer", cpu=True)
    for round in range(ROUNDS):
        player.roll(get_user_roll())
        cpu.roll()
        player_result, cpu_result = player.rolls[-1].against(cpu.rolls[-1])
        player.new_result(player_result)
        cpu.new_result(cpu_result)
        tprint(f"Round   {round + 1}")
        if player.record[-1] == WIN:
            tprint("You win!")
            tprint(f"{player.rolls[-1].name}   beats   {cpu.rolls[-1].name}")
        elif player.record[-1] == LOSE:
            tprint("You   lose!")
            tprint(f"{cpu.rolls[-1].name}   beats   {player.rolls[-1].name}")
        else:
            tprint("It's   a   tie!")
            tprint(f"Both   chose   {player.rolls[-1].name}")
    # If there is a tie, the player wins
    winner = player if sum(player.record) >= sum(cpu.record) else cpu
    tprint(f"In {ROUNDS} rounds, {winner.name} won!")


if __name__ == "__main__":
    main()

