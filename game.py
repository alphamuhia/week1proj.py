import random

def get_computer_choice():
    return random.choice(["r", "p", "s"])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "r" and computer == "s") or \
         (player == "p" and computer == "r") or \
         (player == "s" and computer == "p"):
        return "player"
    else:
        return "computer"

def display_choice(choice):
    return {"r": "rock", "p": "paper", "s": "scissors"}.get(choice, "unknown")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    
    rounds_played = 0
    player_score = 0
    computer_score = 0
    
    while rounds_played < 3:
        player_choice = input("Enter 'r' for 'rock', 'p' for 'paper', or 's' for 'scissors' (or 'q' to exit):\n ").lower()
        
        if player_choice == "q":
            print("Thanks for playing!")
            return
        elif player_choice not in ["r", "p", "s"]:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"You chose: {display_choice(player_choice)}")
        print(f"Computer chose: {display_choice(computer_choice)}")
        
        result = determine_winner(player_choice, computer_choice)
        if result == "player":
            print("You win the round!")
            player_score += 1
        elif result == "computer":
            print("Computer wins the round!")
            computer_score += 1
        else:
            print("This round is a tie!")
        
        rounds_played += 1
        print(f"Score: You {player_score} - {computer_score} Computer\n")
    
    # Determine the overall winner
    if player_score > computer_score:
        print("Congratulations! You are the winner of the best of three!")
    elif computer_score > player_score:
        print("The computer wins! Better luck next time.")
    else:
        print("It's a tie!")
    print("Game over. Thanks for playing!")

if __name__ == "__main__":
    main()
