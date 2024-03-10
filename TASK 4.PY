import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def print_result(user_choice, computer_choice, winner):
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    if winner == 'tie':
        print("It's a tie!")
    else:
        print(f"{winner.capitalize()} wins!")

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        winner = determine_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, winner)
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        print(f"Score - User: {user_score}, Computer: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

play_game()