import random
import time

game = ["rock","paper","scissors"]
player = True

while player == True:
    computer = random.choice(game)
    guess = input("What do you choose, Rock, Paper, or, scissors:").lower()
    if guess == "scissors":
        if computer == "Rock":
            print("The computer chose ", computer)
            time.sleep(2)
            print("You chose ", guess)
            time.sleep(2)
            print("You Lose")
            player == False
        elif computer == "paper":
            print("The computer chose ", computer)
            time.sleep(2)
            print("You chose ", guess)
            time.sleep(2)
            print("You win")
            player == False
        elif computer == "scissors":
            print("The computer chose ", computer)
            time.sleep(2)
            print("You chose ", guess)
            time.sleep(2)
            print("You tied")
            player == False
    if guess == "rock":
        if computer == "Rock":
            print("The computer chose ", computer)
            time.sleep(2)
            print("You chose ", guess)
            time.sleep(2)
            print("You tie")
            time.sleep(2)
            player == False
        elif computer == "paper":
            print("The computer chose ", computer)
            time.sleep(2)
            print("You chose ", guess)
            time.sleep(2)
            print("You lose")
            player == False
        elif computer == "scissors":
            print("The computer chose ", computer)
            time.sleep(2)
            print("You chose ", guess)
            time.sleep(2)
            print("You win")
            player == False
    if guess == "paper":
        if computer == "Rock":
            print("The computer chose ", computer)
            time.sleep(2)
            print("You chose ", guess)
            time.sleep(2)
            print("You win")
            player == False
        elif computer == "paper":
            print("The computer chose ", computer)
            time.sleep(2)
            print("You chose ", guess)
            time.sleep(2)
            print("You tie")
            player == False
        elif computer == "scissors":
            print("The computer chose ", computer)
            time.sleep(2)
            print("You chose ", guess)
            time.sleep(2)
            print("You lose")
            player == False



