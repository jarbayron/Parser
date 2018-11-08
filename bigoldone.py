import definer
import myfunc
import os
from myfunc import pdfsep,textfiledlt,pdffiledlt
from definer import listmaker

def king(pdf):
    textfiledlt()
    pdffiledlt()
    pdfsep(pdf)
    import texter
    a=[]
    b=0
    for filename in os.listdir(r'C:\Users\Bayron\Desktop\Money\43placidln\Textfiles'):
        if filename.endswith('.txt'):
            raw=list(filter(None, [elem.strip('\n') for elem in open(r'C:\Users\Bayron\Desktop\Money\43placidln\Textfiles\\'+filename).readlines()]))
            for item in raw:
                if ('$' in item)==True:
                    a.append(raw[:])
                    b=b+1
                    break
            settled=[]
            active=[]
            for elem in a:
                bl=''.join(elem)
                if ('Settled Date' in bl)==True:
                    settled.append(elem[:])
                else:
                    active.append(elem[:])
    return settled,active

a=[]
b=0
for filename in os.listdir(r'C:\Users\Bayron\Desktop\Money\43placidln\Textfiles'):
    if filename.endswith('.txt'):
        raw=list(filter(None, [elem.strip('\n') for elem in open(r'C:\Users\Bayron\Desktop\Money\43placidln\Textfiles\\'+filename).readlines()]))
        for item in raw:
            if ('$' in item)==True:
                a.append(raw[:])
                b=b+1
                break
        settled=[]
        active=[]
        for elem in a:
            bl=''.join(elem)
            if ('Settled Date' in bl)==True:
                settled.append(elem[:])
            else:
                active.append(elem[:])


        


       



##liste=listmaker('36.txt','3630.txt','36.txt')
##listone=liste[0]
##listtwo=liste[1]
##listthree=liste[2]






