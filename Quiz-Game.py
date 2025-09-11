print(" Welcome to the Quiz Game 📚")

questions = {
    "What’s the capital of Japan? ": "tokyo",
    "First programming language ever created? ": "fortran",
    "Which country invented pizza? ": "italy",
    "What does HTTP stand for? ": "hypertext transfer protocol",
    "Fastest land animal in the world? ": "cheetah"
}

score = 0

for q, a in questions.items():
    ans = input(q).lower()
    if ans == a:
        print("W move ✅")
        score += 1
    else:
        print("L bruh ❌ The right answer is:", a)

print(f"\nFinal Score: {score}/{len(questions)}")
if score == len(questions):
    print("Sheeesh 🤯 100% correct, you built different!")
elif score >= 3:
    print("Not bad bruh, mid but passable 😎")
else:
    print("💀 Study harder, bruh… this ain’t it.")
