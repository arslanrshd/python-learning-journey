import random

def fun_game():
    global user_wins,computer_wins,ties
    computer_input = ["Snake", "Water", "Gun"]
    computer = random.choice(computer_input)
    player = input("Enter Snake, Water, or Gun: ").strip().capitalize()
    if player not in computer_input:
        print("Invalid input. Please enter Snake, Water, or Gun.")
    elif player == computer:
        print(f"It's a tie: both you and the computer chose {player}")
        ties+=1
    elif ((player=="Snake" and computer=="Gun") or
          (player=="Gun" and computer=="Water") or
          (player=="Water" and computer=="Snake")):
        print(f"You Lose: because your input is {player} and computer input is {computer}")
        computer_wins+=1
    elif ((player=="Snake" and computer=="Water") or 
         (player=="Water" and computer=="Gun") or   
         (player=="Gun" and computer=="Snake")):
         print(f"You Win: because your input is {player} and computer input is {computer}")
         user_wins+=1

user_wins = 0
computer_wins = 0
ties = 0
fun_game()
while True:
    play_again = input("Do you want play again? (yes/no): ").strip().lower()
    if play_again.lower()=="yes":
        fun_game()
    elif play_again.lower()=="no":
        print(f"You win {user_wins} time.")
        print(f"Computer win {computer_wins} time.")
        print(f"Ties {ties} time.")
        print("Thanks for playing!")
        break
    else:
        print("Invalid input, please type 'yes' or 'no'.")