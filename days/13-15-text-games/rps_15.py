from rps import Roll, main

ROLLS = [
    "Rock",
    "Gun",
    "Lightning",
    "Devil",
    "Dragon",
    "Water",
    "Air",
    "Paper",
    "Sponge",
    "Wolf",
    "Tree",
    "Human",
    "Snake",
    "Scissors",
    "Fire",
]

if __name__ == "__main__":
    Roll.pos_rolls = ROLLS
    main("BATTLE\nROYALE")
