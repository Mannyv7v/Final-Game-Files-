#Emmanuel Velazquez
#This is the final chapter.. here, the user faces the toughest foes, and hardest puzzles for the final and strongest piece of the elden ring.
def use_elden_ring_to_overcome_challenges():
    print("Welcome to the Forbidden Caverns!")

    # Use the Elden Ring shards to overcome elemental challenges and puzzles
    print("You encounter strong elemental challenges and puzzles.")
    while True:
        elden_ring_decision = input("Use the Elden Ring shards to overcome challenges? (yes/no): ").lower()
        if elden_ring_decision == "yes":
            print("The Elden Ring shards empower you, allowing you to overcome the elemental challenges.")
            break
        elif elden_ring_decision == "no":
            print("You choose not to use the Elden Ring shards. The elemental forces prove too strong, and you face consequences.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def battle_elemental_guardians():
    print("You face epic battles with elemental guardians.")
    print("These guardians protect the last shard of the Elden Ring.")
    while True:
        battle_decision = input("Engage in the battle with elemental guardians? (yes/no): ").lower()
        if battle_decision == "yes":
            print("You engage in epic battles and successfully defeat the elemental guardians.")
            break
        elif battle_decision == "no":
            print("You choose not to engage in the battle. The elemental guardians overwhelm you, and you face consequences.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def uncover_hidden_chambers():
    print("You explore the forbidden caverns and uncover hidden chambers.")
    print("These chambers may contain artifacts with god-like powers and the last shard of the Elden Ring.")
    while True:
        uncover_decision = input("Explore the hidden chambers? (yes/no): ").lower()
        if uncover_decision == "yes":
            print("You successfully uncover hidden chambers, finding artifacts and the last shard of the Elden Ring.")
            break
        elif uncover_decision == "no":
            print("You choose not to explore the hidden chambers. The secrets remain undiscovered, and you face consequences.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def claim_victory():
    print("Congratulations! You have successfully completed Chapter 5.")
    print("You harness the powers of the Elden Ring, liberating Eldoria!")

def chapter_5():
    # Use the Elden Ring shards to overcome elemental challenges and puzzles
    use_elden_ring_to_overcome_challenges()

    # Battle elemental guardians
    battle_elemental_guardians()

    # Uncover hidden chambers to find artifacts and the last shard of the Elden Ring
    uncover_hidden_chambers()

    # Check if the player is successful in all actions and is ready to claim victory
    while True:
        victory_decision = input("Do you wish to claim victory and liberate Eldoria? (yes/no): ").lower()
        if victory_decision == "yes":
            claim_victory()
            break
        elif victory_decision == "no":
            print("You choose not to claim victory. The journey continues...")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

