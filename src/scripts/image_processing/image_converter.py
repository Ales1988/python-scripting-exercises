"""
This script converts images inside a folder from jpeg to png
Run the script from the terminal giving origin folder and destination folder as parameter:
python {path}/image_converter.py {origin_path} {destination folder name}"
"""

import sys
from pathlib import Path
from image_utils import create_destination_folder, run_conversion

# Reciving arguments
origin_folder = sys.argv[1]
destination_folder = sys.argv[2]

# Convert the origin folder path from string to a pathlib.Path object
origin_path = Path(origin_folder)

# Handling destination path and creating destination folder
destination_path = create_destination_folder(origin_path, destination_folder)

run_conversion(origin_path, destination_path)
