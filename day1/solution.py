# %%
import requests
import os
# %%
cookies = {"session": os.environ.get('SESSION_COOKIE')}  # TODO: set your Advent of Code session cookie
response = requests.get("https://adventofcode.com/2022/day/1/input", cookies=cookies)
# %%
elfs = response.text.split("\n\n")

elfs_total_calories = []
for i in elfs:
    elfs_total_calories.append(sum([int(x) for x in i.splitlines()]))

print(f"Top elf carrying {max(elfs_total_calories)} calories")

elfs_total_calories.sort(reverse=True)

print(f"Top 3 elfs carrying {sum(elfs_total_calories[0:3])} calories")

