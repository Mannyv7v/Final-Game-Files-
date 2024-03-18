#Emmanuel velazquez
#Chapter 3
import random
import Chapter4

def use_moonstone():
    print("You find a mysterious moonstone in the Whispering Woods.")
    print("It radiates a soft glow. What action do you take?")
    use_moonstone_decision = input("Use the moonstone to reveal the safe passage? (yes/no): ").lower()

    if use_moonstone_decision == "yes":
        print("The moonstone reveals the safe passage through the magical traps.")
    else:
        print("You chose not to use the moonstone. Unfortunately, you trigger a deadly trap and meet your demise.")

def interact_with_spirits():
    print("You encounter spirits of ancient sorcerers in the ruins.")
    print("They offer clues on navigating the shifting corridors.")
    interact_decision = input("Interact with the spirits for clues? (yes/no): ").lower()

    if interact_decision == "yes":
        print("The spirits provide valuable clues, guiding you through the shifting corridors.")
    else:
        print("You decide not to interact with the spirits. Unfortunately, you get lost in the shifting corridors.")

def navigate_ruins():
    print("Welcome to the Ruins of Lysandria!")

    # Use the moonstone to reveal the safe passage
    use_moonstone()

    # Interact with spirits for clues on navigating the shifting corridors
    interact_with_spirits()

    # Determine if the player successfully navigates the ruins or faces consequences
    if random.choice([True, False]):
        print("Congratulations! You successfully navigate the shifting corridors.")
        print("You discover a golden chest with the Elden Ring shard inside.")
    else:
        print("Unfortunately, you fail to navigate the shifting corridors and face dire consequences.")

def start_chapter_4():
    print("Congratulations! You have successfully completed Chapter 3.")
    print("Welcome to Chapter 4!")
    Chapter4.chapter_4()

def chapter_3():
    navigate_ruins()

    # Check if the player is ready to start Chapter 4
    while True:
        continue_journey = input("Do you wish to continue your journey to Chapter 4? (yes/no): ").lower()
        if continue_journey == "yes":
            start_chapter_4()
            break
        elif continue_journey == "no":
            print("You decide to stay in the Ruins of Lysandria. The journey continues...")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


