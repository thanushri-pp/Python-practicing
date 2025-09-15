import random

print("✨ Welcome to the Word Scrambler ✨")

def scramble(word):
    return "".join(random.sample(word, len(word)))

while True:
    text = input("\nEnter a word to scramble (or type 'quit'): ")
    if text.lower() == "quit":
        print("Exiting... scrambled vibes over 👋")
        break
    print("Scrambled word:", scramble(text))
