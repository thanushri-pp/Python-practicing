import time

print("⌨ Welcome to Typing Speed Tester ⌨️")
print("Type the sentence below as fast as you can, bruh:\n")

sentence = "bruh coding at 3am hits different fr"
print(f"👉 {sentence}\n")

input("Press Enter when you're ready... ")

start = time.time()
typed = input("\nStart typing: ")
end = time.time()

time_taken = end - start
words = len(sentence.split())
wpm = round((words / time_taken) * 60)

print(f"\nYou took {round(time_taken, 2)} seconds.")
if typed == sentence:
    print(f"🔥 Accuracy 100% | Speed: {wpm} WPM")
else:
    print(f"Bruh, you messed up the text 💀 | Speed: {wpm} WPM")
