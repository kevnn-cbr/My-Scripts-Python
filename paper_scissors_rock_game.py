import random

def play_game():
    options = ["rock", "paper", "scissors"]
    
    print("--- ROCK, PAPER, SCISSOR GAME ---")
    user_choice = input(" Choose rock, paper, or scissor: ").lower()
    
    #The computer picks one option from the list 
    computer_choice = random.choice(options)
    
    print(f"Computer chose:{computer_choice}")
    
    #The logic to decide who wins 
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
       print("You win! Hacker skills activated.")
    else:
        print("Computer wins! Try again.")
 #Start the match
play_game()
