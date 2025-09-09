import random
import string

print(" Random Password Generator 🔐")

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    try:
        length = int(input("\nEnter password length (min 4, max 30): "))
        if length < 4 or length > 30:
            print("Choose a length between 4 and 30.")
            continue
        print("Your generated password is:", generate_password(length))
    except ValueError:
        print("Enter a valid number!")
    
    again = input("Generate another? (y/n): ").lower()
    if again != "y":
        print("Bye! Stay safe online. 🔒")
        break
