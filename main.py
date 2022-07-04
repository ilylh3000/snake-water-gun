import random

while True:
    choices = ["snake", "water", "gun"]

    AI = random.choice(choices)
    Player = None

    while Player not in choices:
        Player = input ("snake, water, or gun?: ").lower()

    if Player == AI:
        print("AI: ", AI)
        print("Player: ", Player)
        print("Tie!")
    elif Player == "snake":
        if AI == "gun":
            print("AI: ", AI)
            print("Player: ", Player)
            print("You Lose!") 
        if AI == "water":
            print("AI: ", AI)
            print("Player: ", Player)
            print("You Win!")
    elif Player == "gun":
        if AI == "water":
            print("AI: ", AI)
            print("Player: ", Player)
            print("You Lose!") 
        if AI == "snake":
            print("AI: ", AI)
            print("Player: ", Player)
            print("You Win!")
    elif Player == "water":
        if AI == "snake":
            print("AI: ", AI)
            print("Player: ", Player)
            print("You Lose!") 
        if AI == "gun":
            print("AI: ", AI)
            print("Player: ", Player)
            print("You Win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Thank You for playing withe me; human :)")