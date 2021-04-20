import random
import time
# Initial Steps to invite in the game:
print("\nWelcome to Hangman Game\n")
name = input("Enter your name: ")
print("Hello " + name + "! Good Luck!")
time.sleep(3)
print("Are you Ready!!\n Let's play Hangman!")
time.sleep(2)
def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()
