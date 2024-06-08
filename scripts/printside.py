from glob import glob
from os.path import basename
import sys
import toml

mods = [file for file in glob("../mods/*.toml")]
sides = [x.lower() for x in sys.argv]

for filepath in mods:
    toml_file = toml.load(filepath)
    filename = basename(filepath).split(".")[0]
    side = toml_file['side']

    if side == "both" and side in sides:
         print(f"This is a both-sided mod: {toml_file['name']} | {filename} ")
    elif side == "server" and side in sides:
         print(f"This is a server-sided mod: {toml_file['name']} | {filename} ")
    elif side == "client" and side in sides:
        print(f"This is a client-sided mod: {toml_file['name']} | {filename}")
