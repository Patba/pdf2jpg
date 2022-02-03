import sys
from pdf2image import convert_from_path
import glob, os
import os, subprocess

#from pathlib import Path

pdf_dir = os.getcwd()
os.chdir(pdf_dir)

print(pdf_dir)

for pdf_file in glob.glob(os.path.join(pdf_dir, "*.pdf")):
    pages = convert_from_path(pdf_file, poppler_path = ".\dep\poppler")
    print(pdf_file)
    for page in pages:
        page.save(pdf_file[:-4] +".jpg", 'JPEG')
