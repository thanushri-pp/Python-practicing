import random

print("🎲 Welcome to Dice Roller 🎲")
print("Type 'y' to roll or 'n' to dip, bruh.")

while True:
    choice = input("\nYou wanna roll? (y/n): ").lower()
    
    if choice == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"Bruh... you rolled {dice1} and {dice2}.")
        
        if dice1 == dice2:
            print("No way bruh 😱 That’s doubles. You lucky today.")
        else:
            print("Mid roll tbh, try again 💀")
            
    elif choice == "n":
        print("Aight bruh, game over. Catch you later 👋")
        break
    else:
        print("Bruh that ain’t valid. Type 'y' or 'n'.")
