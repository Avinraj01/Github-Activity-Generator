import os
import random
from datetime import datetime, timedelta

# date input function
def get_date_input():
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    return datetime.strptime(start, "%Y-%m-%d"), datetime.strptime(end, "%Y-%m-%d")

# simple commits
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

# intensity commits
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

# pattern commits (basic)
def pattern_commits(start_date, end_date, text):
    delta = end_date - start_date
    pattern_days = len(text)

    for i in range(delta.days + 1):
        date = start_date + timedelta(days=i)

        if i < pattern_days:
            commits = 6
        else:
            commits = 1

        for j in range(commits):
            with open("data.txt", "a") as f:
                f.write(f"{date} pattern {j}\n")

            os.system("git add .")
            os.system(f'git commit --date="{date}" -m "pattern commit {j}"')

# main menu
print("Choose option:")
print("1. Simple commits")
print("2. Intensity control")
print("3. Pattern (text)")

choice = input("Enter choice (1/2/3): ")

start_date, end_date = get_date_input()

if choice == "1":
    simple_commits(start_date, end_date)

elif choice == "2":
    level = input("Enter intensity (low/medium/high): ").lower()
    intensity_commits(start_date, end_date, level)

elif choice == "3":
    text = input("Enter text (e.g. AVIN): ")
    pattern_commits(start_date, end_date, text)

else:
    print("Invalid choice")

os.system("git branch -M main")
os.system("git push -u origin main")