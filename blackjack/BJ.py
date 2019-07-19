'''Example student code. They need to calculate the point value of a pokerhand,
given as a list of poker cards, listed as suit, then number (ie: eight of spades is S8)'''
def calculatePoints(hand):
    sum = 0
    numAces = 0
    for card in hand:
        if(card[1] == "A"):
            sum += 11
            numAces +=1
        elif(card[1] == "K" or card[1] == "Q" or card[1] == "J" or card[1] == "T"):
            sum += 10
        else:
            sum += int(card[1])
    while(sum > 21 and numAces > 0):
        sum -= 10
        numAces -= 1
    return sum
