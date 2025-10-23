# python -m unittest discover -s tests

import unittest
from pathlib import Path

from src.scripts.image_processing import image_utils


class TestImageUtils(unittest.TestCase):
    # Tests if run_conversion tries to convert something different from an image
    def test_invalid_file(self):
        origin_path = Path(__file__).parent / "test_origin"
        destination_path = Path(__file__).parent / "test_destination"
        image_utils.run_conversion(origin_path, destination_path)


if __name__ == "__main__":
    unittest.main()
