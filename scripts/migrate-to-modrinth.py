from glob import glob
import requests
import subprocess
import toml
import os
from time import sleep
import logging

logging.basicConfig(filename='app.log', level=logging.INFO, filemode="w")

session = requests.Session()
headers = {
    'User-Agent': "scotus-1/migrate-cf-to-mr.py"
}
modrinth_search_url = 'https://api.modrinth.com/v2/search?facets=[["project_type:mod"]]&query='
modpack_file_path = os.path.expandvars("%AppData%\\PrismLauncher\\instances\\fcsp")

for filepath in glob(modpack_file_path + '\\mods\\*.toml'):
    toml_file = toml.load(filepath)

    if toml_file['update'].get('curseforge', False):
        filename = os.path.basename(filepath).split(".")[0]
        mod_name = toml_file['name']

        response = session.get(modrinth_search_url + filename, headers=headers).json()
        hits = response["hits"]
        if len(hits) > 0:
            main_mod = hits[0]
            logging.info(f"Found mod on curseforge: {mod_name} / {filename} -> {main_mod['title']} / {main_mod['slug']}")
            subprocess.run(["packwiz", "remove", filename], cwd=modpack_file_path)

            logging.info(f"Removing {filename}.pw.toml")
            subprocess.run(["packwiz", "mr", "add", main_mod['slug']], cwd=modpack_file_path)
            logging.info(f"Adding modrinth version")
        else:
            logging.error(f"Modrinth not found for mod: {filename} / {mod_name}")

        sleep(0.5)
    else:
        logging.warning(f"Skipped {toml_file['name']}: Already on modrinth")

