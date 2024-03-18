#Emmanuel velazquez
#Chapter 2 involves arrival to the whispering woods and fighting guardians protecting the elden ring fragment behind puzzles.
import Chapter3
def discover_scriptures():
    print("As you explore the Whispering Woods, you discover ancient scriptures.")
    print("You learn more about the history and lore of the Elden Ring.")

def fight_guardians():
    print("You encounter guardians protecting a fragment of the Elden Ring.")

def solve_puzzle_with_elden_ring():
    print("You come across a mystical puzzle in the Whispering Woods.")
    print("The Elden Ring resonates with the puzzle. What action do you take?")

def start_chapter_3():
    print("Congratulations! You have successfully completed Chapter 2.")
    print("Welcome to Chapter 3!")
    Chapter3.chapter_3()

def chapter_2():
    print("Welcome to Chapter 2 - The Whispering Woods!")

    # Discover new scriptures and learn the lore of the ring
    discover_scriptures()

    # Fight guardians to obtain a fragment of the Elden Ring
    fight_guardians()

    # Solve a puzzle using the Elden Ring
    solve_puzzle_with_elden_ring()

    # Check if the player is ready to start Chapter 3
    while True:
        continue_journey = input("Do you wish to continue your journey to Chapter 3? (yes/no): ").lower()
        if continue_journey == "yes":
            start_chapter_3()
            break
        elif continue_journey == "no":
            print("You decide to stay in the Whispering Woods. The journey continues...")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

