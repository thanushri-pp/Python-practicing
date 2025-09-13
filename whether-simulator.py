import random
import time

print(" Welcome to the Bruh Weather Simulator 🌦️")

forecasts = [
    "Bruh it’s raining code snippets 💻🌧️",
    "Hot like your GPU after gaming 🔥",
    "Cloudy with 100% chance of procrastination ☁️",
    "Snowing bugs in your code ❄️🐛",
    "Windy… brace your WiFi connection 🌬️📶",
    "Sunny with main character vibes 🌞✨"
]

while True:
    city = input("\nEnter your city (or type 'quit' to exit): ")
    if city.lower() == "quit":
        print("Aight bruh, weather vibes ended 👋")
        break
    print(f"Weather in {city}: {random.choice(forecasts)}")
    time.sleep(1)
