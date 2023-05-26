import csv
import os
import requests

# Step 1: Download the CSV file
csv_url = "https://raw.githubusercontent.com/dgibbs64/SteamCMD-AppID-List/main/steamcmd_appid.csv"
response = requests.get(csv_url)
csv_data = response.text

# Step 2: Create the "Mapping" folder if it doesn't exist
mapping_folder = "Mapping"
if not os.path.exists(mapping_folder):
    os.makedirs(mapping_folder)

# Step 3: Process the CSV file and create symbolic links
csv_reader = csv.reader(csv_data.splitlines())
next(csv_reader)  # Skip the header row

for row in csv_reader:
    folder_name = row[0]
    link_name = row[1]

    folder_path = f"./{folder_name}"
    link_path = f"./{mapping_folder}/{link_name}"

    if os.path.exists(folder_path) and not os.path.exists(link_path):
        os.symlink(os.path.abspath(folder_path), link_path)
        print(f"Created symbolic link: {link_path} -> {os.path.abspath(folder_path)}")
    elif not os.path.exists(folder_path):
        pass
    else:
        print(f"Symbolic link already exists: {link_path}")

print("Symbolic link creation completed.")
