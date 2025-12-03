p1 = input("Player 1, enter your move (rock/paper/scissors): ")
p2 = input("Player 2, enter your move (rock/paper/scissors): ")

if p1 == "rock":
    if p2 == "rock":
        print("It's a tie!")
    else:
        if p2 == "paper":
            print("Player 2 wins!")
        elif p2 == "scissors":
            print("Player 1 wins!")
        else:
            print("Invalid move by Player 2")
elif p1 == "paper":
    if p2 == "paper":
        print("It's a tie!")
    else:
        if p2 == "rock":
            print("Player 1 wins!")
        elif p2 == "scissors":
            print("Player 2 wins!")
        else:
            print("Invalid move by Player 2")
elif p1 == "scissors":
    if p2 == "scissors":
        print("It's a tie!")
    else:
        if p2 == "paper":
            print("Player 1 wins!")
        elif p2 == "rock":
            print("Player 2 wins!")
        else:
            print("Invalid move by Player 2")
else:
    print("Invalid move by Player 1")
