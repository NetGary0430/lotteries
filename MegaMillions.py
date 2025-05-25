import pandas as pd
import requests
from pypdf import PdfReader
import tabula
import os
from downloadANDread import download_and_read_pdf

# Read PDF into list of DataFrame
inputPDF = "megaMILL.pdf"

pdf_url = "https://files.arizonalottery.com/past-180-days/Past180Days_Mega_Millions.pdf" # Example URL
output_file = ("megaMILL.pdf")
download_and_read_pdf(pdf_url, output_file)

pdf_path = inputPDF
pdf_file = open(pdf_path, 'rb')
pdf_reader = PdfReader(pdf_file)

tables = []
for page_num in range(len(pdf_reader.pages)):
    table = tabula.read_pdf(pdf_path, pages=page_num + 1, stream=True)[0]
    tables.append(table)

df = pd.concat(tables, ignore_index=True)

print(df)
outputPDF = "D:\\MyCode\\python\\W2calculator\\lotto_results\\Mega_Millions.xlsx"
df.to_excel(outputPDF)