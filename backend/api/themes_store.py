import os
import json
import Millennium

def is_valid(theme_native_name: str) -> bool:

    folder_path = os.path.join(Millennium.steam_path(), "steamui", "skins", theme_native_name)
    file_path = os.path.join(folder_path, "skin.json")

    if not os.path.exists(folder_path) or not os.path.isfile(file_path):
        return False

    try:
        with open(file_path, 'r') as file:
            json.load(file)
    except json.JSONDecodeError:
        return False

    return True

def find_all_themes() -> str:

    themes = [] 
    path = Millennium.steam_path() + "/steamui/skins"

    if not os.path.exists(path):
        os.makedirs(path)

    filenames = os.listdir(path)
    subdirectories = [filename for filename in filenames if os.path.isdir(os.path.join(path, filename))]
    subdirectories.sort()

    for theme in subdirectories:
        skin_json_path = os.path.join(path, theme, "skin.json")

        if not os.path.exists(skin_json_path):
            continue

        with open(skin_json_path, 'r') as json_file:
            
            try:
                skin_data = json.load(json_file)
                themes.append({"native": theme, "data": skin_data})

            except json.JSONDecodeError:
                print(f"Error parsing {skin_json_path}. Invalid JSON format.")

    return json.dumps(themes)
