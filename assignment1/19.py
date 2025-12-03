print("Welcome to the Haunted House")
direction = input("Do you want to go upstairs or downstairs? ")
if direction == "downstairs":
    print("Game Over")
elif direction == "upstairs":
    choice1 = input("Do you want to enter the room or stay outside? ")
    if choice1 == "enter the room":
        print("Game Over")
    elif choice1 == "stay outside":
        creature = input("Choose between ghost, vampire, or werewolf: ")
        if creature == "werewolf":
            print("You Win")
        elif creature in ["ghost", "vampire"]:
            print("Game Over")
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")
else:
    print("Invalid direction")