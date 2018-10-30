import random


class Creature:
    def __init__(self, name, level):
        if not isinstance(name, str):
            raise TypeError("Creature name must be a string")
        if not isinstance(level, int):
            raise TypeError("level must be an int")
        self.name = name
        self.level = level

    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self.level


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        if not isinstance(scaliness, int):
            raise TypeError("Scaliness must be an int")
        self.scaliness = scaliness
        self.breaths_fire = bool(breaths_fire)

    def defensive_roll(self):
        roll = super().defensive_roll()
        value = roll * self.scaliness
        if self.breaths_fire:
            value = value * 2

        return value


class Wizard(Creature):
    def attack(self, creature):
        my_roll = self.defensive_roll()
        their_roll = creature.defensive_roll()

        return my_roll >= their_roll
