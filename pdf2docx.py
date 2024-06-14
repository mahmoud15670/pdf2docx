from pdf2docx import Converter

# Path to the new PDF file
pdf_file_path_new = '/mnt/data/MCQ of technology hematological analysis  second term.pdf'

# Path to the DOCX file
docx_file_path_new = '/mnt/data/MCQ_of_technology_hematological_analysis_second_term_v2.docx'

# Convert PDF to DOCX
cv = Converter(pdf_file_path_new)
cv.convert(docx_file_path_new, start=0, end=None)
cv.close()

# Confirm the conversion by checking the output file
import os
os.path.exists(docx_file_path_new)
