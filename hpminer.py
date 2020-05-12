import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
            
        text = fake_file_handle.getvalue()    
    
    converter.close()
    fake_file_handle.close()
    print()
    print(text)

def extract_text_from_txt(filename):
    myfile=open(filename,"rt")
    contents=myfile.read()
    myfile.close()
    print()
    print(contents)

def extract_data_from_web(name):
    #Shreyas add your code here
    
if __name__ == '__main__':
    name=input("Enter file name with extension (or enter url):")
    p=name[-3::]
    if(p=="pdf"):
        extract_text_from_pdf(name)
    elif(p=="txt"):
        extract_text_from_txt(name)
    else:
        extract_data_from_web(name)
        
