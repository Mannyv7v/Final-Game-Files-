#Emmanuel Velazquez
#Chapter 1 - CSS 225 game
import Chapter2
class GameChapter:
    def __init__(self):
        self.response = []
        self.npcName = ""

    def Get_Character_Name(self):
        character_name = input("What is your name? ")
        return character_name

    def Hooded_Figure_Intro(self, character_name):
        print("Welcome!", character_name, "A hooded figure approaches you.")
        print("Hooded Figure: Greetings traveler! You are the chosen one destined to break the curse on Eldoria")
        print("Hooded Figure: I am known as the guide, what is your name,", character_name,"?")

    def talk_to_locals(self):
        print("You decide to talk to locals in Eldoria to gather info on the Elden Ring")
        self.response = ["You seek the ring... eh? Long ago, a beast was owner of the Elden Ring. He attempted to master its god-like powers, but it became too much to handle. The ring exploded, with it still on the user's hand. Legend says the ring lives in fragments scattered throughout the land. Here's a map to an alleged location of one of the shards.."]

        self.npcName = "Radahn"

        print(self.npcName, ": The name is", self.npcName, "Got time to chat?")
        answer = input("Press y to talk to " + self.npcName)
        if answer == "y":
            print(self.npcName, ":]", self.response)
        else:
            print(self.npcName, ":] Goodbye!")

    def Start_Chapter_2(self):
        print("You have received the map to the Whispering Woods")
        print("This concludes Chapter 1, Start Chapter 2")
        Chapter2.chapter_2()

    def Chapter_1(self):
        print("Welcome to Chapter 1")
        # Get Character name
        character_name = self.Get_Character_Name()

        # Intro by the Hooded figure
        self.Hooded_Figure_Intro(character_name)

        # Talk to locals
        self.talk_to_locals()

        # Check if the user wants to start chapter 2
        travel_decision = input("Would you like to travel to the Whispering Woods? Yes/No?")
        if travel_decision.lower() == "yes":
            self.Start_Chapter_2()
        else:
            print("You decide to stay in Eldoria, the journey continues...")

# Instantiate the class and call Chapter_1 to start the game
game = GameChapter()
game.Chapter_1()