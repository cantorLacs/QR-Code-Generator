import qrcode
from PIL import Image
import openpyxl
import os

# Load the Excel workbook
book = openpyxl.load_workbook("Book1.xlsx", data_only=True)
sheet = book.active

# Get the number of rows and define the cells to read
row_count = sheet.max_row
rowA = "A1"  # First row of column A
rowB = "B" + str(row_count)  # Last row of column B
cells = sheet[rowA:rowB]

# Create a list to store the codes
codes = []

# Read data from the Excel file
for row in cells:
    code = [cell.value for cell in row]
    codes.append(code)

# Create a folder to save the images if it doesn't exist
output_dir = "QR_Codes"
os.makedirs(output_dir, exist_ok=True)

# Generate and save the QR codes
for code in codes:
    qr_image = qrcode.make(str(code[0]))  # Generate the QR code
    file_name = os.path.join(output_dir, f"{code[1]}.png")  # File name
    qr_image.save(file_name)  # Save the image

print("Done!!")
