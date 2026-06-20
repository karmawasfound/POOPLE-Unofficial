import random

BROWN = "\033[38;5;94m"
RESET = "\033[0m"

inp = ""
last_word = ""
steps = 0

def validity():
    global inp, last_word
    while True:
        if len(inp) != 4:
            inp = input("Try again\nEnter a 4-letter word: ").strip().upper()
            continue
        if inp not in word_pool:
            inp = input("Try again\nEnter a 4-letter word: ").strip().upper()
            continue
        if last_word:
            diff = sum(1 for i in range(4) if inp[i] != last_word[i])
            if diff != 1:
                inp = input(f"Try again\n'{inp}' must differ by exactly 1 letter from '{last_word}': ").strip().upper()
                continue
        break

def checkbrown():
    global inp
    colored = []
    for i in range(4):
        if inp[i] == anslist[i]:
            colored.append(f"{BROWN}{inp[i]}{RESET}")
        else:
            colored.append(inp[i])
    print("".join(colored))


with open("words.txt", "r") as file:
    word_pool = [line.strip().upper() for line in file.readlines() if len(line.strip()) == 4]

ans = "POOP"
anslist = list(ans)
last_word = random.choice(word_pool)
inp = last_word
steps = 0

print("Welcome to POOPLE unofficial!")
print(f"Goal: reach '{ans}' in as few steps as possible.")
print("Each new word must be a valid 4‑letter word and differ by exactly one letter from the previous one.")
print("Your starting word: ")
checkbrown()

while inp != ans:
    inp = input("Next word: ").strip().upper()
    validity()
    checkbrown()
    last_word = inp
    steps += 1

print(f"You win! Reached in {steps} steps.\n")
