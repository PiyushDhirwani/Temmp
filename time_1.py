from pdf2image import convert_from_path

# Convert the first page of the PDF to a PNG image
images = convert_from_path('Testing.pdf', dpi=200, first_page=1, last_page=1)
image = images[0]

# Save the image as a PNG file
image.save('output.png', 'PNG')


import io
import PyPDF2
import pytesseract
from PIL import Image

# Open the input image file
image = Image.open('output.png')

# Convert the image to grayscale
image = image.convert('L')

# Use Tesseract to extract text from the image
text = pytesseract.image_to_string(image)

# Create a new PDF writer
writer = PyPDF2.PdfFileWriter()

# Create a new page with the extracted text
new_page = PyPDF2.pdf.PageObject.createBlankPage(None, image.width, image.height)
new_page.addContent(PyPDF2.pdf.ContentStream([PyPDF2.pdf.TextObject(text)]))

# Add the new page to the output PDF file
writer.addPage(new_page)

# Write the output PDF file
with open('output.pdf', 'wb') as output_file:
    writer.write(output_file)