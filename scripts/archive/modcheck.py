import webbrowser

path = "modlist.txt"

with open(path, 'r') as file:
    for line in file.readlines():
        if line.startswith("https://www.curseforge"):
            webbrowser.open(line + "/files/all", 2)
            print("Opened: " + line)
        elif line.startswith("https://modrinth"):
            webbrowser.open(line + "/versions", 2)
            print("Opened " + line)
        else:
            webbrowser.open(line, 2)
            print("Opened" + line)
