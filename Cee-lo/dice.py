import random

class Die:

    def __init__(self, num_sides):
        self._num_sides = num_sides
        self._last_side = -1

    def roll(self):
        self._last_side = random.randint(1, self._num_sides)
        return self._last_side

    def current_roll(self):
        return self._last_side

    def __str__(self):
        return "A die with " + str(self._num_sides) + " sides"

class Dice:

    def __init__(self, num_dice, num_sides):
        self._num_dice = num_dice
        self._num_sides = num_sides
        self._dice = []
        for i in range(self._num_dice):
            self._dice.append(Die(self._num_sides))

    def roll_all(self):
        results = []
        for die in self._dice:
            results.append(die.roll())
        return results

    def reroll(self, index):
        return self._dice[index].roll()

    def current_roll(self):
        results = []
        for die in self._dice:
            results.append(die.current_roll())
        return results

    def __str__(self):
        return str(self._num_dice) + " dice with " + str(self._num_sides) + " sides"
