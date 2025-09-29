import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") \
         or (user == "paper" and computer == "rock") \
         or (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def main():
    print("🎮 Welcome to Rock-Paper-Scissors! 🎮")
    
    user_score = 0
    computer_score = 0
    
    while True:
        # User input
        user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("⚠️ Invalid choice. Please enter rock, paper, or scissors.")
            continue
        
        # Computer choice
        computer_choice = get_computer_choice()
        print(f"🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")
        
        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        
        if result == "tie":
            print("🤝 It's a tie!")
        elif result == "user":
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("😢 Computer wins this round.")
            computer_score += 1
        
        # Show score
        print(f"📊 Score => You: {user_score} | Computer: {computer_score}")
        
        # Play again option
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\n👋 Thanks for playing Rock-Paper-Scissors!")
            break

if __name__ == "__main__":
    main()