"""
This script add a watermark to each page of a pdf file.
To run the script:
python src/scripts/pdf_watermarker/main.py resources/pdf_watermarker/{file.pdf}
resources/pdf_watermarker/{watermarker.pdf}

Output in resources/pdf_watermarker/watermarked.pdf
"""

from pypdf import PdfWriter, PdfReader
from pathlib import Path
import sys


def watermarker(pdf_file: Path, watermark_file: Path) -> str:
    if not pdf_file.is_file() or not watermark_file.is_file():
        print("ERRRROOOOR")
        return "Error: missing or invalid file."

    stamp = PdfReader(watermark_file).pages[0]
    writer = PdfWriter(clone_from=pdf_file)
    for page in writer.pages:
        page.merge_page(stamp, over=False)  # here set to False for watermarking

    writer.write("resources/pdf_watermarker/watermarked.pdf")
    return "Watermark added to pdf file."


pdf_file = Path(sys.argv[1])
watermark_file = Path(sys.argv[2])

if __name__ == "__main__":
    result = watermarker(pdf_file, watermark_file)
    print(result)
