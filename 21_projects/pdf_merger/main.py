
from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []

n = int(input("How many pdf do you want merge?\n"))

for i in range(0,n):
    name = input(f"Entger the name of pdf{i + 1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("mergedPDF.pdf")

merger.close()