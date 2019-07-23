#create a function called "whoWins" which takes in 3 player cards and 3 dealer card values, and decide who wins the match
def whoWins(playerCardOne, playerCardTwo, playerCardThree, dealerCardOne, dealerCardTwo, dealerCardThree):
    playerSum = playerCardOne + playerCardTwo + playerCardThree
    dealerSum = dealerCardOne + dealerCardTwo + dealerCardThree
    if(playerSum % 10 > dealerSum % 10):
        print("The player wins")
    else:
        print("The dealer wins")
