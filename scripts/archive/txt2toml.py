import subprocess

path = "modlist.txt"

with open(path, 'r') as file:
    for line in file.readlines():
        if line.startswith("https://www.curseforge"): mode = "cf"
        elif line.startswith("https://modrinth"): mode = "mr"
        print(f"\n{line}")
        subprocess.call(["packwiz", mode, "install", line.strip("\n")])
        print("\n")


