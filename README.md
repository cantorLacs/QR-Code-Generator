# QR Code Generator

This project generates QR codes from data stored in an Excel file (`Book1.xlsx`). Each QR code is saved as a PNG image in a dedicated directory.

![image](https://github.com/user-attachments/assets/46da0997-4f43-47f0-9d93-6ffc4cadfbf6)

## Features

- Reads data from an Excel file.
- Generates QR codes for each entry.
- Saves QR codes in a separate folder (`QR_Codes`).

## Prerequisites

To run this project, you need to have Python installed along with the following libraries:

- `qrcode`
- `Pillow`
- `openpyxl`

## Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/youruserna
2. Change to the project directory:
   ```bash
   cd your-repository
3. Install the required libraries:
   ```bash
   pip install qrcode[pil] openpyxl
4. Place your Book1.xlsx file in the same directory as the script.

# Usage

1. Ensure your Book1.xlsx file is formatted correctly. The script expects the QR code data in column A and corresponding file names in column B.

2. Run the script:
   ```bash
    python generate_qr.py
   
3. After execution, check the QR_Codes folder for the generated QR code images.

## Example of `Book1.xlsx` Format

| QR Code Data | File Name |
|--------------|-----------|
| 1234567890   | Code1     |
| 9876543210   | Code2     |

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
qrcode for QR code generation.
Pillow for image handling.
openpyxl for Excel file operations.


