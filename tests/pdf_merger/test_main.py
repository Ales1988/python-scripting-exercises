# To run the tests, run this in the root project folder
# python -m unittest discover -s tests

import unittest
from pathlib import Path
from src.scripts.pdf_merger import main


class TestMergePdf(unittest.TestCase):
    # When passing a not existing file to the script
    def test_file_notexists(self):
        inputs = [Path("notafile.pdf")]
        main.pdf_combiner(inputs)


if __name__ == "__main__":
    unittest.main()
