import random

emoji_map = {
    "bruh": "😎",
    "hello": "👋",
    "love": "❤️",
    "code": "💻",
    "sleep": "😴",
    "fire": "🔥",
    "food": "🍔",
    "music": "🎶",
    "laugh": "😂",
    "cat": "🐱",
    "dog": "🐶"
}

print("🎉 Welcome to the Bruh Emoji Translator 🎉")

while True:
    text = input("\nType something (or 'quit' to exit): ").lower()
    if text == "quit":
        print("Aight bruh, no more emojis 👋")
        break
    words = text.split()
    translated = [emoji_map.get(word, word) for word in words]
    print("👉", " ".join(translated))
