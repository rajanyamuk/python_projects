from pdf2docx import Converter

old_pdf = "pdf_to_docx_converter\\python_study_material.pdf"
new_doc = "new_file.docx"

obj = Converter(old_pdf)
obj.convert(new_doc)