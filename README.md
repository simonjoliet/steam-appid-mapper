# steam-appid-mapper
The Steam App ID Mapper is a Python script that automates the creation of symbolic links for Proton Steam Application IDs (app IDs). It fetches a CSV file containing app ID mappings and their corresponding names, and creates symbolic links between existing folders and a designated "Mapping" folder.

# Features
* Loads a CSV file containing Steam app ID mappings
* Creates a "Mapping" folder if it doesn't exist
* Creates symbolic links between existing folders and the "Mapping" folder based on CSV data
* Provides feedback on the creation of symbolic links

# Usage
1. Ensure you have Python installed on your system.
2. Clone the repository or download the "steam-appid-mapper.py" script into your steamapps compatdata repository. For instance on the Steam Deck:

`#Internal storage
/home/deck/.steam/steam/steamapps/compatdata

#MicroSD drive
/run/media/mmcblk0p1/steamapps/compatdata`

4. Install the necessary dependencies by running the following command:

`pip install requests`

Note: pip is not installed by default on the Steam Deck, you can instead use:

```
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
if [ -d "$HOME/.local/bin" ]; then
  PATH="$HOME/.local/bin:$PATH"
fi
```

4. Run the script using the following command:

`python steam-appid-mapper.py`

# Configuration
The script does not require any configuration. However, you can modify the csv_url variable in the script to use a different URL for the CSV file if needed.

# Acknowledgements
The app ID mappings used in this script are sourced from dgibbs64/SteamCMD-AppID-List. Many thanks to the project contributors for maintaining the CSV file.

# Contributing
Contributions to the Steam App ID Mapper are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

# Disclaimer
This script is provided as-is without any warranty. Use it at your own risk.

Feel free to customize the README file based on your specific needs and add any additional sections or information that may be relevant to your project.
