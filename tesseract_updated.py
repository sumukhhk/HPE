import pytesseract
import os
def extract_text_from_image(img_name):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    text=pytesseract.image_to_string(img_name)
    return text
enteries=os.listdir('images_tesseract')
file_no=1
for img in enteries:    
    f=open(str(file_no)+".txt","w")
    data=extract_text_from_image(img)
    f.write(data)
    file_no+=1
    f.close()
    
