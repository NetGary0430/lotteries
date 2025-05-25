import pandas as pd
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re
from pypdf import PdfReader
import tabula
import os


# url = "https://files.arizonalottery.com/past-180-days/Past180Days_Mega_Millions.pdf"
# response = requests.get(url)
# htmlData = response.content
# parsedData = BeautifulSoup(htmlData, "html.parser")

# from pathlib import Path
# import requests
# filename = Path('Past180Days_Mega_Millions.pdf')
# url = "https://files.arizonalottery.com/past-180-days/Past180Days_Mega_Millions.pdf"
# response = requests.get(url)
# filename.write_bytes(response.content)
# print(filename)

# Import libraries
import requests
from bs4 import BeautifulSoup

# URL from which pdfs to be downloaded
url = "https://www.arizonalottery.com/draw-games/mega-millions/"

# Requests URL and get response object
response = requests.get(url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')

# Find all hyperlinks present on webpage
links = soup.find_all('a')

i = 0

# From all links check for pdf link and
# if present download file
for link in links:
    if ('.pdf' in link.get('href', [])):
        i += 1
        print("Downloading file: ", i)

        # Get response object for link
        response = requests.get(link.get('href'))

        # Write content in pdf file
        pdf = open("pdf"+str(i)+".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        print("File ", i, " downloaded")


print("All PDF files downloaded")