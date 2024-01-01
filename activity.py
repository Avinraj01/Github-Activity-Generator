import os
import random
from datetime import datetime, timedelta

# ------------------ FONT MAP ------------------
FONT = {
    "A": [" 1 ", "1 1", "111", "1 1", "1 1"],
    "B": ["11 ", "1 1", "11 ", "1 1", "11 "],
    "C": [" 11", "1  ", "1  ", "1  ", " 11"],
    "D": ["11 ", "1 1", "1 1", "1 1", "11 "],
    "E": ["111", "1  ", "11 ", "1  ", "111"],
    "F": ["111", "1  ", "11 ", "1  ", "1  "],
    "G": [" 11", "1  ", "1 1", "1 1", " 11"],
    "H": ["1 1", "1 1", "111", "1 1", "1 1"],
    "I": ["111", " 1 ", " 1 ", " 1 ", "111"],
    "J": ["111", "  1", "  1", "1 1", " 1 "],
    "K": ["1 1", "1 1", "11 ", "1 1", "1 1"],
    "L": ["1  ", "1  ", "1  ", "1  ", "111"],
    "M": ["1 1", "111", "111", "1 1", "1 1"],
    "N": ["1 1", "111", "111", "111", "1 1"],
    "O": ["111", "1 1", "1 1", "1 1", "111"],
    "P": ["111", "1 1", "111", "1  ", "1  "],
    "Q": ["111", "1 1", "1 1", "111", "  1"],
    "R": ["111", "1 1", "111", "1 1", "1 1"],
    "S": ["111", "1  ", "111", "  1", "111"],
    "T": ["111", " 1 ", " 1 ", " 1 ", " 1 "],
    "U": ["1 1", "1 1", "1 1", "1 1", "111"],
    "V": ["1 1", "1 1", "1 1", " 1 ", " 1 "],
    "W": ["1 1", "1 1", "111", "111", "1 1"],
    "X": ["1 1", " 1 ", " 1 ", " 1 ", "1 1"],
    "Y": ["1 1", " 1 ", " 1 ", " 1 ", " 1 "],
    "Z": ["111", "  1", " 1 ", "1  ", "111"],

    "0": ["111", "1 1", "1 1", "1 1", "111"],
    "1": [" 1 ", "11 ", " 1 ", " 1 ", "111"],
    "2": ["111", "  1", "111", "1  ", "111"],
    "3": ["111", "  1", "111", "  1", "111"],
    "4": ["1 1", "1 1", "111", "  1", "  1"],
    "5": ["111", "1  ", "111", "  1", "111"],
    "6": ["111", "1  ", "111", "1 1", "111"],
    "7": ["111", "  1", " 1 ", " 1 ", " 1 "],
    "8": ["111", "1 1", "111", "1 1", "111"],
    "9": ["111", "1 1", "111", "  1", "111"]
}

# ------------------ DATE INPUT ------------------
def get_date_input():
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    return datetime.strptime(start, "%Y-%m-%d"), datetime.strptime(end, "%Y-%m-%d")


# ------------------ SIMPLE ------------------
def simple_commits(start, end):
    delta = end - start
    for i in range(delta.days + 1):
        date = start + timedelta(days=i)
        for _ in range(random.randint(1, 3)):
            with open("data.txt", "a") as f:
                f.write(str(date))
            os.system("git add .")
            os.system(f'git commit --date="{date}" -m "simple commit"')


# ------------------ INTENSITY ------------------
def intensity_commits(start, end, level):
    levels = {"low": (1,2), "medium": (2,4), "high": (4,7)}
    min_c, max_c = levels.get(level, (1,3))

    delta = end - start
    for i in range(delta.days + 1):
        date = start + timedelta(days=i)
        for _ in range(random.randint(min_c, max_c)):
            with open("data.txt", "a") as f:
                f.write(str(date))
            os.system("git add .")
            os.system(f'git commit --date="{date}" -m "intensity commit"')


# ------------------ PATTERN ------------------
def pattern_commits(start, end, text):
    text = text.upper()

    grid = []
    for r in range(5):
        line = ""
        for ch in text:
            if ch in FONT:
                line += FONT[ch][r] + "  "
        grid.append(line)

    positions = set()
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "1":
                positions.add((r, c))

    delta = (end - start).days

    for i in range(delta + 1):
        date = start + timedelta(days=i)
        row = date.weekday()
        col = i // 7

        if (row % 5, col % len(grid[0])) in positions:
            commits = random.randint(5,8)
        else:
            continue

        for _ in range(commits):
            with open("data.txt", "a") as f:
                f.write(str(date))
            os.system("git add .")
            os.system(f'git commit --date="{date}" -m "pattern {text}"')


# ------------------ MAIN ------------------
print("\nChoose option:")
print("1. Simple commits")
print("2. Intensity control")
print("3. Pattern (ANY text)")

choice = input("Enter choice: ")

start, end = get_date_input()

if choice == "1":
    simple_commits(start, end)

elif choice == "2":
    level = input("Enter intensity (low/medium/high): ")
    intensity_commits(start, end, level)

elif choice == "3":
    text = input("Enter text (A-Z, 0-9): ")
    pattern_commits(start, end, text)

else:
    print("Invalid choice")

os.system("git branch -M main")
os.system("git push -u origin main")

print("✅ Done! Check GitHub 🚀")