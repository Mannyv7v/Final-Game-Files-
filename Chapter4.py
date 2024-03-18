#Emmanuel Velazquez
#Chapter 4
import Chapter5

def consult_seer():
    print("Welcome to the Mystic Citadel!")

    # Consult the seer to gain cryptic insights
    print("You approach the magical seer in the floating city.")
    while True:
        seer_decision = input("Consult the seer for insights? (yes/no): ").lower()
        if seer_decision == "yes":
            print("The seer provides cryptic insights about the next Elden Ring shard.")
            print("The seer also mentions forbidden caverns as the alleged location of the last shard.")
            break
        elif seer_decision == "no":
            print("You decide not to consult the seer. The journey continues without additional insights.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def engage_in_rituals():
    print("You decide to engage in rituals to unlock the latent powers of the Elden Ring shards.")
    while True:
        rituals_decision = input("Performing the rituals may enhance your abilities. Engage in rituals? (yes/no): ").lower()
        if rituals_decision == "yes":
            print("You successfully perform rituals and unlock latent powers.")
            break
        elif rituals_decision == "no":
            print("You choose not to engage in rituals. Your powers remain as they were.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def start_chapter_5():
    print("Congratulations! You have successfully completed Chapter 4.")
    print("Welcome to Chapter 5!")
    Chapter5.chapter_5()

def chapter_4():
    # Consult the seer and gain insights
    consult_seer()

    # Engage in rituals to unlock latent powers
    engage_in_rituals()

    # Check if the player is ready to start Chapter 5
    while True:
        continue_journey = input("Do you wish to continue your journey to Chapter 5? (yes/no): ").lower()
        if continue_journey == "yes":
            start_chapter_5()
            break
        elif continue_journey == "no":
            print("You decide to stay in the Mystic Citadel. The journey continues...")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
