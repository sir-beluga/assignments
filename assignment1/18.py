print("Welcome to the Magic Forest")
direction = input("Do you want to go north or south? ")
if direction == "south":
    print("Game Over")
elif direction == "north":
    choice1 = input("Do you want to cross the river or follow the path? ")
    if choice1 == "cross the river":
        print("Game Over")
    elif choice1 == "follow the path":
        creature = input("Choose between fairy, ogre, or elf: ")
        if creature == "elf":
            print("You Win")
        elif creature in ["fairy", "ogre"]:
            print("Game Over")
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")
else:
    print("Invalid direction")
