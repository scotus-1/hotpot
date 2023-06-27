import shutil
import os
import subprocess

try:
    os.mkdir("./generated")
except FileExistsError:
    shutil.rmtree("./generated")
    os.mkdir("./generated")


def generate_files_from_folder_selective(basePath, files, modscopy=False):
    os.makedirs(f"./generated/{basePath}", exist_ok=True)
    for file in files:
        if modscopy == True:
            file += ".pw.toml"
        shutil.copyfile(f"../{basePath}{file}", f"./generated/{basePath}{file}")


rootFiles = [".packwizignore"]
paxiResourcePacks = ["13.zip", "Stardust Labs Omni-Biome Name Fix v1.5-1.19.zip", "xali's+Enchanted+Books+v0.12.0.zip", "xali's+Potions+v1.0.zip"]
bothSidedMods = ['accurate-block-placement', 'auditory', 'addadd', 'additionz', 'advancement-frames', 'air-hop', 'another-furniture', 'antighost', 'appleskin', 'aquatic-torches', 'architectury-api', 'armor-statues', 'autotag', 'axes-are-weapons', 'axolotl-bucket-fix', 'balm', 'beautified-chat-client', 'beautify-refabricated', 'bedspreads', 'beenfo', 'beneath-the-snow', 'better-biome-blend', 'better-stats', 'better-third-person', 'better-tridents', 'bits-and-chisels', 'cake-chomps', 'cammies-minecart-tweaks', 'capybara-fabric', 'cc-restitched', 'celestria', 'chefs-delight', 'chimes', 'chunky', 'cleancut', 'clickthrough', 'cloth-api', 'cloth-config', 'clumps', 'collective', 'colorfulanvils', 'comforts', 'completeconfig', 'compostable-rotten-flesh', 'connectible_chains', 'controlling', 'couplings', 'crafting-tweaks', 'create-fabric', 'ct-overhaul-village', 'cyanide-fabric', 'deathlog', 'debugify', 
'deepslatecutting', 'diagonal-fences', 'diagonal-panes', 'displaycase', 'do-a-barrel-roll', 'easy-anvils', 'easy-magic', 'easy-shulker-boxes', 'editsign', 'enchanted-vertical-slabs', 'expanded-delight', 'expanded-trident-enchanting', 'fabric-disable-custom-worlds-advice', 'fabric-seasons-delight-compat', 'fabric-seasons-extras', 'fabric-seasons', 'farmers-delight-fabric', 'farmers-knives', 'farmers-respite-fabric', 'fast-furnace-for-fabric', 'ferrite-core', 'fish-on-the-line', 'forge-config-api-port', 'fwaystones', 'gliders', 'handcrafted', 'herdspanic', 'horse-expert', 'horsebuff', 'iceberg', 'immersive-paintings', 'immersive-weathering', 
'inmis', 'inmisaddon', 'inspecio', 'inventory-totem', 'itemswapper', 'jade-addons-fabric', 'jade', 'jamlib', 'joy-of-painting', 'jumpy-boats-fabric', 'keepheadnames', 'kiwi', 'krypton', 'labels', 'lazydfu', 'leaves-be-gone', 'library-ferret-fabric', 'lithium', 'loud-leads', 'magnum-torch', 'malilib', 'mavapi', 'mavm', 'memoryleakfix', 'midnightlib', 'minihud', 'mixin-conflict-helper', 'mixintrace', 'mob-scarecrows', 'monsters-in-the-closet', 
'moonlight', 'more-banner-features', 'more-mob-variants', 'more-villagers-fabric', 'mru', 'natures-compass', 'nicephore-fabric', 'no-chat-reports', 'no-strip', 'nullscape', 'owo-lib', 'patchouli', 'paxi', 'pick-up-notifier', 'playeranimator', 'pling', 'prism-lib', 'projectsavethepets', 'puzzles-lib', 'pyrotastic', 'qkl', 'qsl', 'quit', 'recipe-cache', 'rei', 'replanter', 'resourceful-lib', 'searchables', 'shiny-horses', 'show-me-what-you-got', 'show-me-your-skin', 'simple-voice-chat', 'supplementaries', 'talkbubbles', 'terralith', 'the-lost-castle', 'things', 'thorium', 'torch-hit', 'trinkets', 'universal-enchants', 'universal-graves', 'variant-bookshelves-fabric', 'visual-overhaul', 'visual-workbench', 'voidtotem', 'yacl', 'yosbr', "yungs-api", "xaeros-world-map", "xaeros-minimap", "way2wayfabric", "soul-fire-d"]
clientSidedMods = ['advancementinfo',
'axolotl-buckets', 'better-mount-hud', 'better-ping-display-fabric', 'betterf3', 'chat-heads', 'colormatic', 'craftify', 'craftpresence', 
'cull-less-leaves', 'cullclouds', 'dashloader', 'dcch', 'dynamic-fps', 'ebe', 'enchanting-table-descriptions', 'enhanced-searchability', 'entityculling', 'fabric-seasons-terralith-compat', 'fastquit', 'indium', 'invmove', 'iris', 'item-model-fix', 'keybinds', 'modmenu', 'morechathistory', 'moreculling', 'no-resource-pack-warnings', 'puzzle', 'quickconnectbutton', 'quilt-loading-screen', 'reeses-sodium-options', 'satin-api', 'sodium-extra', 'sodium', 'statssearch', 'tooltipfix', 'vtdownloader', 'zoomify', 'cit-resewn', 'modmenu', 'visuality']
mods = bothSidedMods + clientSidedMods

shutil.copytree("../config/yosbr", "./generated/config/yosbr")
print("Copied YOSBR Folder")

generate_files_from_folder_selective("", rootFiles)
print("Copied Root Files")

generate_files_from_folder_selective("config/paxi/resourcepacks/", paxiResourcePacks)
print("Copied Paxi Resourcepacks")

generate_files_from_folder_selective("mods/", mods, modscopy=True)
print("Copied Mods")

shutil.copyfile(f"./index.toml", f"./generated/index.toml")
shutil.copyfile(f"./pack.toml", f"./generated/pack.toml")
print("Copied pack.toml and index.toml")

subprocess.run(['packwiz', 'refresh'], cwd="./generated/")