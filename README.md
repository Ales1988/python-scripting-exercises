# Python Scripting Exercises

Collections of scripts based on "The Complete Python Developer" course by Andrei Neagoie. This is a learning project for practicing Python.

Note: Unit tests and data validation are partial; this project is for learning purposes only and does not cover every scenario.

## Scripts

### 1. Image Processing
Converts images from JPEG to PNG.
Run the script in the project root: 
python src/scripts/image_processing/image_converter.py {origin_path} {destination_folder}

Where:
- origin_path is the path to the folder with jpeg files
- destination_folder is the destination folder name

Note: destination folder will be create at the same level as the origin folder

### 2. Pdf merger
Merges two or more pdf files.
Run the script in the project root: 
python src/scripts/pdf_merger/main.py {pdf1 path} {pdf2 path} {pdf3 path}

Note: destination folder is project_root/resources/pdf_merger/merged.pdf"

### 3. Pdf watermarker
This script add a watermark to each page of a pdf file.
To run the script:
python src/scripts/pdf_watermarker/main.py resources/pdf_watermarker/{file.pdf}
resources/pdf_watermarker/{watermarker.pdf}

Note: output in resources/pdf_watermarker/watermarked.pdf