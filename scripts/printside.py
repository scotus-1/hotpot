from glob import glob
from os.path import basename
import os
import sys
import toml
from zipfile import *
import json

mods = [file for file in glob("../mods/*.toml")]
sides = [x.lower() for x in sys.argv]

instance_map_name = "fcsp-localdevserver"
mods_folder_path = f"{os.getenv('APPDATA')}\\PrismLauncher\\instances\\{instance_map_name}\\.minecraft\\mods\\"

def getid(path):
    try: 
        with ZipFile(path, "r") as z:
            try:
                with z.open("fabric.mod.json") as f:
                    return json.loads(f.read(), strict=False)['id']
            except KeyError:
                with z.open("quilt.mod.json") as f:
                    return json.loads(f.read(), strict=False)['quilt_loader']['id']
    except FileNotFoundError:
        return("n/a")
                
for filepath in mods:
    toml_file = toml.load(filepath)
    filename = basename(filepath).split(".")[0]
    filepath = mods_folder_path + toml_file['filename']
    side = toml_file['side']

    if side == "both" and side in sides:
         print(f"This is a both-sided mod: {toml_file['name']} | {filename}  | {getid(filepath)}")
    elif side == "server" and side in sides:
         print(f"This is a server-sided mod: {toml_file['name']} | {filename} | {getid(filepath)}")
    elif side == "client" and side in sides:
        print(f"This is a client-sided mod: {toml_file['name']} | {filename} | {getid(filepath)}")
