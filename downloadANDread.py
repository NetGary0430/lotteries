import requests
from pypdf import PdfReader
import os
import time

url = "https://www.arizonalottery.com/draw-games/mega-millions/"


def download_and_read_pdf(url, output_path):
    """Downloads a PDF from a URL, tracks download completion, and then reads the PDF."""

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Track download progress (example: check file size)
        total_size = int(response.headers.get('content-length', 0))  # Get the total size (if available)
        downloaded = 0

        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):  # Set chunk size for efficiency
                if chunk:  # filter out keep-alive new chunks
                    file.write(chunk)
                    downloaded += len(chunk)
                    # Optionally, track download progress (e.g., print percentage)
                    if total_size > 0:
                        percentage = (downloaded / total_size) * 100
                        print(f"Downloaded: {percentage:.2f}%")
                    else:
                        print("Downloading...")

        print("Download complete.")

        # Wait for download completion (optional, but can be helpful)
        time.sleep(1)  # Give a short delay to ensure download is complete

        # Read the PDF
        try:
            with open(output_path, 'rb') as pdf_file:
                pdf = PdfReader(pdf_file)
                num_pages = len(pdf.pages)
                print(f"Number of pages: {num_pages}")
                # You can then extract text, metadata, etc. from the PDF using the PyPDF2 library
                # Example:
                # for i in range(num_pages):
                #     page = pdf.pages[i]
                #     text = page.extract_text()
                #     print(f"Page {i+1}:\n{text}\n")
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return

    except requests.exceptions.RequestException as e:
        print(f"Error during download: {e}")
        return
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
pdf_url = "https://files.arizonalottery.com/past-180-days/Past180Days_Mega_Millions.pdf"
output_file = ("megaMILL.pdf")
download_and_read_pdf(pdf_url, output_file)
