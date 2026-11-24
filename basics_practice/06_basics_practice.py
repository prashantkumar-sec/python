
from pypdf import PdfReader
import os

pdf_file = input("Enter PDF file path: ")

if os.path.exists(pdf_file):
    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text + "\n\n"

    output_file = os.path.splitext(pdf_file)[0] + ".txt"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

    print("PDF converted successfully!")
    print(f"Text file saved as: {output_file}")

else:
    print("PDF file not found!")
