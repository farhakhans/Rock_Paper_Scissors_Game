import random

def play_game():
    # Ask the user for their choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Ensure the input is valid
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        return

    # Randomly choose for the computer
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose! Try again.")

# Run the game
play_game()
