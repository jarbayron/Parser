from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import logging
import shutil


def pdfsep(thing):
    inputpdf = PdfFileReader(open(thing,"rb"))
    for i in range(inputpdf.numPages):
        output=PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\pdfs\\document-page%s.pdf" % i, "wb") as outputStream:
              output.write(outputStream)

def textfiledlt():
    shutil.rmtree(r'C:\Users\Bayron\Desktop\Money\43placidln\Textfiles')
    b=0
    while b==0:
        try:
             os.makedirs(r'C:\Users\Bayron\Desktop\Money\43placidln\Textfiles')
             b=1
        except:
            pass

def pdffiledlt():
    shutil.rmtree(r'C:\Users\Bayron\Desktop\Money\43placidln\pdfs')
    b=0
    while b==0:
        try:
             os.makedirs(r'C:\Users\Bayron\Desktop\Money\43placidln\pdfs')
             b=1
        except:
            pass

class sron(str):
    def finder( self,xx,yy):
        b=self.find(xx)
        if b==-1:
            return print('error in finding start')   
        c=self.find(yy,b+len(xx))
        if c==-1:
            return print('error in finding end')
        empty=[]
        for i in range(b,c+len(yy)):
            empty.append(self[i])
        return ''.join(empty)
    

class lron(list):
    def finder(self,xx,yy):
        try:
            b=[ind+1 for ind,elem in enumerate(self) if (xx in elem) if (len(elem)==len(xx))==True]
            c=[ind for ind,elem in enumerate(self) if (yy in elem) if (len(elem)==len(yy))==True]
            empty=[]
            for i in range(int(b[0]),int(c[0])):
                empty.append(self[i])
            return ' '.join(empty)
        except:
            print('error in input for finer in lron')

class lsron(list):
    def finder(self,xx,yy):
        telf=' '.join(self)
        b=telf.find(xx)
        if b==-1:
            return print('error in finding start')   
        c=telf.find(yy,b+len(xx))
        if c==-1:
            return print('error in finding end')
        empty=[]
        for i in range(b,c+len(yy)):
            empty.append(telf[i])
        return ''.join(empty)

