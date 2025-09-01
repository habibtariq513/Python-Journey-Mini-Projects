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
duplicates = set()
path = Path('')         
items = list(path.rglob('*'))           # List all files and folders in the current directory

# ========================================== File Input Section ==========================================

print("\n================================== Welcome to PDF Merger! ==================================")
try:
    total_pdfs = int(input("\nHow many PDFs do you want to merge: "))
    if total_pdfs > len(items)-1:  # Exclude the script file itself
        print(f"\n\t**** OOPS! Your Directory has just {len(items) - 1} PDFs. Try again ****")
        exit()
        
    while range(total_pdfs):
        print("\nCurrent Directory Files and Folders:")
        file_folder_path()                                  # Display current directory files and folders        
        pdf = input("\nEnter PDF name: ")
        p = Path(pdf)
        if not p.exists():                                  # Check if the file exists
            print(f"\n\t**** OOPS! {pdf} does NOT exist. Try again ****")
            continue
        if pdf in duplicates:                                 # Check for duplicates
            print(f"\n\t**** OOPS! {pdf} has already been Added. Try again ****")
            continue
        pdfs.append(pdf)
        duplicates.add(pdf)        
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
