import os
import random
from datetime import datetime, timedelta

start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 4, 26)

delta = end_date - start_date

for i in range(delta.days + 1):
    date = start_date + timedelta(days=i)

    commits = random.randint(1, 4)

    for j in range(commits):
        with open("data.txt", "a") as f:
            f.write(f"{date} commit {j}\n")

        os.system("git add .")
        os.system(f'git commit --date="{date}" -m "commit {j}"')

os.system("git branch -M main")
os.system("git push -u origin main")