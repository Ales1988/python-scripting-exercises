"""
Simple pdf merger. Can merge multiple pdf files at the same time.
In the project root, run:
python src/scripts/pdf_merger/main.py resources/pdf_merger/{file.pdf} resources/pdf_merger/{file2.pdf}
"""

import sys
import pypdf
from pathlib import Path

inputs = sys.argv[1:]  # grabs 1 or more inputs from command line


def pdf_combiner(pdf_list):
    writer = pypdf.PdfWriter()

    for pdf in pdf_list:
        path = Path(pdf)
        if not path.is_file() or path.suffix.lower() not in [".pdf"]:
            print(f"File not found {pdf}")
            return "Error: missing or invalid files."  # stop iteration when input isn't a file

        writer.append(pdf)

    writer.write(Path("resources/pdf_merger/merged.pdf"))
    writer.close()
    return "Pdf files merged."


if __name__ == "__main__":
    result = pdf_combiner(inputs)
    print(result)
