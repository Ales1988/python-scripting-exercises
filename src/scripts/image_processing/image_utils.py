# Functions used in the image_converter script

from pathlib import Path
from PIL import Image


def create_destination_folder(origin_path: Path, destination_folder: str) -> Path:
    """
    Creates a destination folder at the same level as origin_path.
    Returns the Path object of the destination folder.
    """
    destination_path = origin_path.parent / destination_folder  # .parent -> parent path
    if destination_path.is_dir():  # check if destination folder exists
        print("Destination folder already exists.")
    else:
        destination_path.mkdir()

    return destination_path


def run_conversion(origin_path: Path, destination_path: Path):
    """
    Converts image files from origin_path to png
    and save them in destination_path
    """
    for file_path in origin_path.iterdir():
        if not file_path.is_file() or file_path.suffix.lower() not in [".jpeg", ".jpg"]:
            print(f"{file_path} isn't a valid file")
            continue  # Skip to next iteration

        print(file_path.stem)  # just the file name without path or extension
        img = Image.open(file_path)
        img.save(destination_path / (file_path.stem + ".png"))
