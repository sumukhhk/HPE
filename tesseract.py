import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
text=pytesseract.image_to_string(r'i2.png')
print(text)
