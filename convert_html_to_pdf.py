import pdfkit
import argparse
import re
from pathlib import Path
from collections import defaultdict
import html
import sys
import os

# --- Configuration ---
# If wkhtmltopdf is not in your system PATH, uncomment the line below
# and set the correct path to the wkhtmltopdf executable.
path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# Define the input HTML file and output PDF file paths
html_file_path = r'c:\Users\garre\Pillar-BS5-v3.1\index.html'
pdf_file_path = r'c:\Users\garre\Pillar-BS5-v3.1\garrett_glick_resume_pdfkit.pdf'

# Options for wkhtmltopdf
options = {
    'enable-local-file-access': None,  # Allows wkhtmltopdf to access local files (CSS, images, etc.)
    'quiet': '', # Suppress wkhtmltopdf output unless error
    'viewport-size': '1280x1024', # Define a viewport size to help with responsive layouts
    'javascript-delay': 5000, # Increased wait time to 5 seconds
    'print-media-type': None, # Use print media type (handles backgrounds in wkhtmltopdf 0.12.x)
    'disable-smart-shrinking': None # Prevent resizing that might break layout
}

# --- Conversion ---
print(f"Converting '{html_file_path}' to PDF...")

try:
    # Use the configuration if you defined it above, otherwise omit the argument
    pdfkit.from_file(html_file_path, pdf_file_path, configuration=config, options=options)

    print(f"Successfully created PDF: '{pdf_file_path}'")

except Exception as e:
    print(f"An error occurred during PDF conversion: {e}")
    print("Ensure wkhtmltopdf is installed and accessible.")
    if 'No wkhtmltopdf executable found' in str(e):
        print("You might need to uncomment and set the 'path_wkhtmltopdf' variable in the script.")
