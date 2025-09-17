print("📊 Word Frequency Counter 📊")

def word_count(text):
    counts = {}
    words = text.split()
    for word in words:
        word = word.lower().strip(".,!?")
        counts[word] = counts.get(word, 0) + 1
    return counts

while True:
    text = input("\nEnter a sentence (or type 'quit'): ")
    if text.lower() == "quit":
        print("Exiting... word counting done 👋")
        break
    counts = word_count(text)
    print("Word frequencies:", counts)
