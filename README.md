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
This script adds a watermark to each page of a pdf file.
To run the script:
python src/scripts/pdf_watermarker/main.py resources/pdf_watermarker/{file.pdf}
resources/pdf_watermarker/{watermarker.pdf}

Note: output in resources/pdf_watermarker/watermarked.pdf

### 4. Email sender
Basic script to send email with python.
In this example, credentials are entered manually via input, as password handling, authentication, and data security are outside the scope of this exercise. 

### 5. Password checker
This script checks if and how many times a password has been leaked.
Run it in the root of the project using:
python src/scripts/password_checker/main.py

The script sends only the first five characters of the password to
pwned api. Then it receives all leaked password whose hashes start
with those characters and uses this response locally to check if input password
has been leaked. It never sends your entire password on the internet.