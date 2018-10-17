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

    def score_delta(self, other_player):
        return sum(self.record) - sum(other_player.record)


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


def play_rounds(player1, player2, rounds=ROUNDS):
    for _ in range(rounds):
        tprint(f"Round   {len(player1.record)+1}")
        player1.roll(get_user_roll())
        player2.roll()
        p1_result, p2_result = player1.rolls[-1].against(player2.rolls[-1])
        player1.new_result(p1_result)
        player2.new_result(p2_result)
        if player1.record[-1] == WIN:
            tprint("You   win!")
            tprint(f"{player1.rolls[-1].name}   beats   {player2.rolls[-1].name}")
        elif player1.record[-1] == LOSE:
            tprint("You   lose!")
            tprint(f"{player2.rolls[-1].name}   beats   {player1.rolls[-1].name}")
        else:
            tprint("It's   a   tie!")
            tprint(f"Both   chose   {player1.rolls[-1].name}")


def main():
    tprint("Rock\nPaper\nSissors", font="Epic")
    name = input("What is your name?:")
    tprint(f"Welcome   {name}!", font="Doom")
    player = Player(name)
    cpu = Player("Computer", cpu=True)
    play_rounds(player, cpu)
    while player.score_delta(cpu) == 0:
        tprint("No winner!\nPlay another round!")
        play_rounds(player, cpu, rounds=1)
    winner = player if player.score_delta(cpu) > 0 else cpu
    tprint(f"In {len(player.record)} rounds, {winner.name} won!")


if __name__ == "__main__":
    main()

