import PyPDF2 as pdf
name=input("Enter the file name (With extension)")
p=name[-3::]
print()
if(p=="pdf"):
    pdf_name=open(name,'rb')
    pdf_obj=pdf.PdfFileReader(pdf_name)
    with open("extracted_data.txt","w") as f:
        for i in range(pdf_obj.getNumPages()):
            data=pdf_obj.getPage(i).extractText()
            f.write(data)
            f.write("\n")
    f=open("extracted_data.txt","r")
    contents=f.read()
    f.close()
    print(contents)

elif(p=="txt"):
    print("This is a text file")
    myfile=open(name,"rt")
    contents=myfile.read()
    myfile.close()
    print(contents)    

else:
    print("The input file is not in pdf or text format")

