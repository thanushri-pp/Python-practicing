print("Palindrome Checker 🔄")

def is_palindrome(word):
    return word == word[::-1]

while True:
    text = input("\nEnter a word (or type 'quit'): ").lower()
    if text == "quit":
        print("Exiting... no more palindrome checks 👋")
        break
    if is_palindrome(text):
        print(f"✅ '{text}' is a palindrome!")
    else:
        print(f"❌ '{text}' is not a palindrome.")
