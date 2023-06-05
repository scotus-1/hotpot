from glob import glob
from os.path import basename
from json import dump

resourcepacks = [basename(file) for file in reversed(glob("../config/paxi/resourcepacks/*.zip"))]

file_data = {
    "loadOrder": resourcepacks
}

print(file_data)

with open("../config/paxi/resourcepack_load_order.json", "w") as out_f:
    dump(file_data, out_f, indent=4)