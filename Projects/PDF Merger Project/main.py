# ========================== Important Notes =========================
# 1. Ensure that the PyPDF2 library is installed in your Python environment. You can install it using pip:
#    'pip install PyPDF2'
# 2. This script merges PDF files in the order they are provided by the user.
# 3. The merged PDF will be saved in the current working directory with the name 'Merged_PDF.pdf'.
# 4. If a specified PDF file does not exist in the current directory, the script will notify the user and exit.

# Use sets for faster duplicate checking, and avoid exiting on a single error.
# Collect all valid PDFs, then merge them at once.


from PyPDF2 import PdfWriter
from pathlib import Path

# Function to display files and folders in the current directory
def file_folder_path():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i + 1}: {item}")

merger = PdfWriter() 
pdfs = []

# ========================================== File Input Section ==========================================

print("\n================================== Welcome to PDF Merger! ==================================")
try:
    total_pdfs = int(input("\nHow many PDFs do you want to merge: "))
    for pdf in range(total_pdfs):
        print("\nCurrent Directory Files and Folders:")
        file_folder_path()                                  # Display current directory files and folders        
        pdf = input("\nEnter PDF name: ")
        p = Path(pdf)
        if p.exists() and pdf not in pdfs:                            # Check if the file exists
            pdfs.append(pdf)
        else:
            print("\n\t**** OOPS! File does NOT exist or It has already been added. Try again ****")
            exit()
except Exception as err:
    print(f"\nError occurred due to {err}\n")

# ========================================== Merging Section ===============================================
print("\nMerging PDFs...")
for pdf in pdfs:
    merger.append(pdf)

merger.write("Merged_PDF.pdf")
print("\nPDFs Merged Successfully into 'Merged_PDF.pdf'")
print("\n\t**** THANK YOU FOR USING PDF MERGER! ****\n")
merger.close()