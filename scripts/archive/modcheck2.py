from glob import glob
from os.path import basename
import requests
import toml
from pywebcopy import save_webpage
import webbrowser

mods = [file for file in glob("../mods/*.toml")]


session = requests.Session()
headers = {
    'User-Agent': "scotus-1/modcheck2.py"
}
modrinth_url = 'https://modrinth.com/mod/'
curseforge_url = 'https://curseforge.com/minecraft/mc-mods/'
for filepath in mods:
    toml_file = toml.load(filepath)
    filename = basename(filepath).split(".")[0]
w
    if toml_file['update'].get('modrinth'):
        download_url = modrinth_url + filename
         # save_webpage(download_url, "./pages", "modcheck2", True, False, False, 1)

    elif toml_file['update'].get('curseforge'):
        download_url = curseforge_url + filename
        webbrowser.open_new_tab(download_url)

    
    
    
    