import random
options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
while True:
    print("\nChoose: rock, paper, or scissors")
    user_move = input("Enter your move: ").lower()

    if user_move not in options:
        print("Invalid move. Please type rock, paper, or scissors.")
        continue

    computer_move = random.choice(options)
    print("Computer chose:", computer_move)    
    if user_move == computer_move:
        print("It's a tie!")
    elif (user_move == "rock" and computer_move == "scissors") or \
         (user_move == "scissors" and computer_move == "paper") or \
         (user_move == "paper" and computer_move == "rock"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1    
    print("Score → You:", user_score, "Computer:", computer_score)
        
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        print("Final Score → You:", user_score, "Computer:", computer_score)
        break
