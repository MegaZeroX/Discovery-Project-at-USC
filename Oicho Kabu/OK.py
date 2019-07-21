'''Example student code. They need to calculate to print whether the dealer or
player wins the hand'''
def whoWins(playerCardOne, playerCardTwo, playerCardThree, dealerCardOne, dealerCardTwo, dealerCardThree):
    playerSum = playerCardOne + playerCardTwo + playerCardThree
    dealerSum = dealerCardOne + dealerCardTwo + dealerCardThree
    if(playerSum % 10 > dealerSum % 10):
        print("The player wins")
    else:
        print("The dealer wins")
