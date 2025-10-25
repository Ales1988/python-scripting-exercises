# To run the tests, run this in the root project folder
# python -m unittest discover -s tests

import unittest
from pathlib import Path
from src.scripts.pdf_watermarker import main


class TestWatermarker(unittest.TestCase):
    # When passing a not existing file to the script
    def test_file_notexists(self):
        pdf_file = Path("notafile.pdf")
        pdf_watermark = Path("notawatermark.pdf")
        result = main.watermarker(pdf_file, pdf_watermark)
        self.assertEqual(result, "Error: missing or invalid file.")


if __name__ == "__main__":
    unittest.main()
