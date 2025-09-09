import random

print("✊ ✋ ✌ Rock-Paper-Scissors Game ✌ ✋ ✊")

options = ["rock", "paper", "scissors"]

while True:
    user = input("\nChoose rock, paper, or scissors (or 'quit' to stop): ").lower()
    
    if user == "quit":
        print("Game over. Thanks for playing! Bruh")
        break
    if user not in options:
        print("Invalid choice, try again!")
        continue

    comp = random.choice(options)
    print(f"Computer chose: {comp}")

    if user == comp:
        print("It's a tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("🔥 You win!")
    else:
        print("💀 HaHaHa I Win!")
