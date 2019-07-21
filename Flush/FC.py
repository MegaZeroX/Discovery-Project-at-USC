def isFlush(cards):
    card_one = cards[0]
    card_two = cards[1]
    card_three = cards[2]
    card_four = cards[3]
    card_five = cards[4]
    if(card_one[0] == card_two[0] and card_one[0] == card_three[0] and card_one[0] == card_four[0] and card_one[0] == card_five[0]):
        return True
    else:
        return False
