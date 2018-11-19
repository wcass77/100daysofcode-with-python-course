import random

import logbook


class Creature:
    def __init__(self, name, level):
        if not isinstance(name, str):
            raise TypeError("Creature name must be a string")
        self.log = logbook.Logger(name)
        self.log.trace(f"Setting up creature...")
        if not isinstance(level, int):
            raise TypeError("level must be an int")
        self.name = name
        self.level = level
        self.log.trace(
            f"{self.name}, a level {self.level} {type(self).__name__}, setup successfully"
        )

    def defensive_roll(self):
        roll = random.randint(1, 12)
        self.log.trace(
            f"{self.name} rolls:{roll}, level:{self.level}. Overall:{roll * self.level}"
        )
        return roll * self.level


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        if not isinstance(scaliness, int):
            raise TypeError("Scaliness must be an int")
        self.scaliness = scaliness
        self.breaths_fire = bool(breaths_fire)
        self.log.trace("Special dragon features set-up successfully")

    def defensive_roll(self):
        roll = super().defensive_roll()
        value = roll * self.scaliness
        if self.breaths_fire:
            value = value * 2
            self.log.trace(f"Dragon breaths fire! overall roll: {value}")
        else:
            self.log.trace(
                f"Dragon doesn't breath fire. Scales protect! overall roll: {value}"
            )
        return value


class Wizard(Creature):
    def attack(self, creature):
        my_roll = self.defensive_roll()
        their_roll = creature.defensive_roll()
        return my_roll >= their_roll
