import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    # Define the valid moves
    moves = ["rock", "paper", "scissors"]

    while True:
        user_move = input("Enter your move (rock, paper, or scissors), or 'q' to quit: ").lower()

        # Check if the user wants to quit the game
        if user_move == 'q':
            print("Thank you for playing. Goodbye!")
            return

        # Check if the user's move is valid
        if user_move not in moves:
            print("Invalid move. Please try again.")
            continue

        # Computer's move
        computer_move = random.choice(moves)

        print(f"You chose: {user_move}")
        print(f"Computer chose: {computer_move}")

        # Determine the winner
        if user_move == computer_move:
            print("It's a tie!")
        elif (user_move == "rock" and computer_move == "scissors") or \
                (user_move == "scissors" and computer_move == "paper") or \
                (user_move == "paper" and computer_move == "rock"):
            print("You win!")
        else:
            print("Computer wins!")

if __name__ == "__main__":
    play_game()
