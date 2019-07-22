from dice import *

class CeeLo:
    def __init__(self):
        self.playerDice = Dice(3, 6)
        self.opponentDice = Dice(3, 6)
        self.player_rolls_remaining = 3
        self.opponent_rolls_remaining = 3

    def roll_all(self):
        if(self.player_rolls_remaining == 0):
            return self.playerDice.current_roll()
        else:
            self.player_rolls_remaining -= 1
            return self.playerDice.roll_all()

    def reroll(self, index):
        if(self.player_rolls_remaining <= 1):
            return self.playerDice.current_roll()
        else:
            self.player_rolls_remaining -= 2
            return self.playerDice.reroll(index)

    def current_rolls(self):
        return self.playerDice.current_roll()

    def get_player_rolls_remaining(self):
        return self.player_rolls_remaining

    def roll_opponent(self):
        self.opponentDice.roll_all()
        score = _score(self.opponentDice.current_roll())
        self.opponent_rolls_remaining -=1
        while(self.opponent_rolls_remaining > 0 and score == 0):
            self.opponentDice.roll_all()
            score = _score(self.opponentDice.current_roll())
            self.opponent_rolls_remaining -=1
        return score

    def opponent_roll(self):
        return self.opponentDice.current_roll()

    def final_score(self):
        return _score(self.playerDice.current_roll()), _score(self.opponentDice.current_roll())

def _score(dice):
    values = dice
    values.sort()
    if(values == [1, 2, 3]):
        return -1
    elif(values == [4, 5, 6]):
        return 13
    elif(values[0] == values[1] and values[0] == values[2]):
        return 6 + values[1]
    elif(values[0] == values[1] or values[0] == values[2] or values[1] == values[2]):
        return values[0]
    else:
        return 0
