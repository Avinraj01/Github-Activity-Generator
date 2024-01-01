import os
import random
from datetime import datetime, timedelta

# ------------------ DATE INPUT ------------------
def get_date_input():
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    return datetime.strptime(start, "%Y-%m-%d"), datetime.strptime(end, "%Y-%m-%d")


# ------------------ SIMPLE COMMITS ------------------
def simple_commits(start_date, end_date):
    delta = end_date - start_date

    for i in range(delta.days + 1):
        date = start_date + timedelta(days=i)
        commits = random.randint(1, 3)

        for j in range(commits):
            with open("data.txt", "a") as f:
                f.write(f"{date} commit {j}\n")

            os.system("git add .")
            os.system(f'git commit --date="{date}" -m "simple commit {j}"')


# ------------------ INTENSITY COMMITS ------------------
def intensity_commits(start_date, end_date, level):
    if level == "low":
        min_c, max_c = 1, 2
    elif level == "medium":
        min_c, max_c = 2, 4
    else:
        min_c, max_c = 4, 7

    delta = end_date - start_date

    for i in range(delta.days + 1):
        date = start_date + timedelta(days=i)
        commits = random.randint(min_c, max_c)

        for j in range(commits):
            with open("data.txt", "a") as f:
                f.write(f"{date} intensity {j}\n")

            os.system("git add .")
            os.system(f'git commit --date="{date}" -m "intensity commit {j}"')


# ------------------ PATTERN COMMITS (REAL GRID BASED) ------------------
def pattern_commits(start_date, end_date, text):
    # 5x7 style font (simplified)
    font = {
        "A": [" 1 ", "1 1", "111", "1 1", "1 1"],
        "V": ["1 1", "1 1", "1 1", " 1 ", " 1 "],
        "I": ["111", " 1 ", " 1 ", " 1 ", "111"],
        "N": ["1 1", "111", "111", "111", "1 1"]
    }

    # build pattern grid
    grid = []
    for row in range(5):
        line = ""
        for ch in text:
            if ch in font:
                line += font[ch][row] + "  "
        grid.append(line)

    # store pattern positions
    pattern_positions = set()
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "1":
                pattern_positions.add((r, c))

    delta = (end_date - start_date).days

    for i in range(delta + 1):
        date = start_date + timedelta(days=i)

        row = date.weekday()  # 0–6 (Mon–Sun)
        col = i // 7

        # map into pattern grid
        if (row % 5, col % len(grid[0])) in pattern_positions:
            commits = random.randint(5, 8)
        else:
            continue  # blank space

        for j in range(commits):
            with open("data.txt", "a") as f:
                f.write(f"{date} pattern {j}\n")

            os.system("git add .")
            os.system(f'git commit --date="{date}" -m "pattern commit {j}"')


# ------------------ MAIN MENU ------------------
print("\nChoose option:")
print("1. Simple commits")
print("2. Intensity control")
print("3. Pattern (text like AVIN)")

choice = input("Enter choice (1/2/3): ")

start_date, end_date = get_date_input()

if choice == "1":
    simple_commits(start_date, end_date)

elif choice == "2":
    level = input("Enter intensity (low/medium/high): ").lower()
    intensity_commits(start_date, end_date, level)

elif choice == "3":
    text = input("Enter text (e.g. AVIN): ").upper()
    pattern_commits(start_date, end_date, text)

else:
    print("Invalid choice")

# push to GitHub
os.system("git branch -M main")
os.system("git push -u origin main")

print("\n✅ Done! Check your GitHub profile 🚀")