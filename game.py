import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def display_choice(choice):
    return {"rock": "rock", "paper": "paper", "scissors": "scissors"}.get(choice, "unknown")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    
    rounds_played = 0
    player_score = 0
    computer_score = 0
    
    while rounds_played < 3:
        player_choice = input("Enter 'rock' for 'rock', 'paper' for 'paper', or 'scisors' for 'scissors' (or 'quit' to exit):\n ").lower()
        
        if player_choice == "quit":
            print("Thanks for playing!")
            return
        elif player_choice not in ["rock", "paper", "scissors"]:
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
