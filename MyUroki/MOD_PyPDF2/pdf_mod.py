import PyPDF2, os
pdf_file = open(os.path.dirname(__file__)+"/"+"tucson.pdf", "rb")

pdf_reader = PyPDF2.PdfFileReader(pdf_file)

print(pdf_reader.numPages)

page_1= pdf_reader.getPage(15)
tt=page_1.extractText()
print(tt.encode("utf-8"))

