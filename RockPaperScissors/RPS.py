'''Example student code. They need to print who wins a rock paper scissors match'''
def rockPaperScissorsWinner(yourChoice, opponentChoice):
    print("You choose " + yourChoice + " and your opponent chooses " + opponentChoice + ", so:")
    if(yourChoice == "rock"):
        if(opponentChoice == "paper"):
            print("Opponent wins")
        elif(opponentChoice == "scissors"):
            print("You win")
        else:
            print("Tie")
    elif(yourChoice == "paper"):
        if(opponentChoice == "scissors"):
            print("Opponent wins")
        elif(opponentChoice == "rock"):
            print("You win")
        else:
            print("Tie")
    else:
        if(opponentChoice == "rock"):
            print("Opponent wins")
        elif(opponentChoice == "scissors"):
            print("You win")
        else:
            print("Tie")
