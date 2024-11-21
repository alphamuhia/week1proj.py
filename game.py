import random

def get_computer_choice():
    return random.choice(["r", "p", "s"])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        player_choice = input("Enter 'r' for 'rock', 'p' for 'paper', or 's' for 'scissors' (or 'q' to exit): ").lower()
        
        if player_choice == "q":
            print("Thanks for playing!")
            break
        elif player_choice not in ["r", "p", "s"]:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
