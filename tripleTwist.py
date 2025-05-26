import pandas as pd
from pypdf import PdfReader
import tabula
from downloadANDread import download_and_read_pdf

# Read PDF into list of DataFrame


pdf_url = "https://files.arizonalottery.com/past-180-days/Past180Days_Triple_Twist.pdf" # Example URL
output_file = "triple_Twist.pdf"
download_and_read_pdf(pdf_url, output_file)

inputPDF = "triple_Twist.pdf"

pdf_path = inputPDF
pdf_file = open(pdf_path, 'rb')
pdf_reader = PdfReader(pdf_file)

tables = []
for page_num in range(len(pdf_reader.pages)):
    table = tabula.read_pdf(pdf_path, pages=page_num + 1, stream=True)[0]
    tables.append(table)

df = pd.concat(tables, ignore_index=True)

print(df)
outputPDF = "D:\\MyCode\\python\\W2calculator\\lotto_results\\tripleTwist.xlsx"
df.to_excel(outputPDF)