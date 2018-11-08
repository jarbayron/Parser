#Purpose of this file is to crete Dictionaries for Listings Possibly Selling,
#make it as Readable and usable for parsing as simply as possible

import re
import pandas as pd
import csv
from myfunc import lron,sron,lsron
raw=0
zips=0
d={}

def braw(self ):
    global raw
    raw=list(filter(None, [elem.strip('\n') for elem in open(self).readlines()]))
   
class rist:
     #Empty Dictionary for us to fill with key items
    #Any form applicable
    global d
    def addressnzip():
        addresses_1= [delem for delem in raw for elem in zips if (elem in delem) == True]
        addresses=[elem for elem in addresses_1 if ('-' in elem)== False]
        
        if not addresses:
            print('Error Finding Applicable NJ Zip code on PDF')
        else:
            [address, ZIP]=addresses[0].split(' NJ')
            d['address']=address+' NJ'
            d['zip']=ZIP
    #Only Listing applicable pending
    def prices():
        assessedprice= raw[[ind for ind,elem in enumerate(raw) if \
                    ('Assessment' in elem)==True][0]+1]

        dollars=[elem for elem in raw if ('$' in elem)==True \
                 if ('/' in elem)== False if (assessedprice in elem)== False]
        if len(dollars) != 2:
            print('Could not find two applicable prices: Relays on ordered pair')
        else:
            d['listing price']= dollars[0]
            d['original price']=dollars[1]
    #REDO Taking Value one up from original price
    def DOM():
        dom= raw[[ind+1 for ind,elem in enumerate(raw) if (d['original price'] in elem)==True][0]].split('/')[0]
        try:
            int(dom)
            d['DOM']=dom
        except:
            print('Error in retrieving DOM: Specifically found non-integer','red')
    #dates taken depending on order       
    def dates():
        smatch=[elem[0] for elem in [re.search('\d{2}/\d{2}/\d{4}', elem) for elem in raw ] if (elem != None)]
        d['original date']=smatch[0]
        d['listing date']=smatch[1]
    #Dpeendent on string 'Age:' positioning
    def age():
        smatch= raw[[ind+1 for ind,elem in enumerate(raw) if ('Age:' in elem)][0]]
        d['age']=smatch
    def floorsnstyle():
        smatch= raw[[ind+1 for ind,elem in enumerate(raw) if ('Design:' in  elem)][0]]
        smatch=re.sub('\D','',smatch)
        if ('2' in smatch)== True:
            design='Colonial'
        elif ('3' in smatch)== True:
            design='Colonial'
        elif ('1.5' in smatch) == True:
            design='Cape'
        else:
            design='Ranch'
            
        d['stories']=smatch
        d['design']=design
        
    def sqft():
        try:
            smatch=[elem for elem in raw if ('Assessor' in elem)]
            smatch=re.sub('\D','', smatch[0])
            if smatch.isdigit()==True: d['sqft']=smatch 
        except:
            print('Error in finding sqft possibly none posted')

    def bednbath():
        try:
            beds=raw[[ind+1 for ind,elem in enumerate(raw) if ('Beds:' in elem)][0]]
            [fb,hb]=raw[[ind+1 for ind,elem in enumerate(raw) if ('Baths:' in elem) if ((len(elem)==6)==True)][0]].split('/')       
            if beds.isdigit()==True: d['number of rooms']=str(int(beds)*2 + 1) 
            if beds.isdigit()==True: d['beds']=beds
            if fb.isdigit()==True: d['full baths']=fb
            if hb.isdigit()==True: d['half baths']=hb
        except:
            print('error in finding baths stuff')
    def type():
        try:
            [unit,attachment]=raw[[ind+1 for ind,elem in enumerate(raw) if ('Type:' in elem)][0]].split('/')
            d['unit']='1' if ('Single' in unit)==True else print('Error not enough input for Single')
            d['attachement']=attachment
        except:
            print('Error in finding string Type:')
    def garage():
        k=lsron(raw).finder('Parking:',':')
        if k.find('No Garage')!= -1:
            b='None'
            parknum='None'
        elif k.find('Attached') != -1:
            if k.find('Car Garage') != -1:
                parknum=re.sub('\D','',sron(k).finder('Parking:','Car Garage'))
            else:
                parknum='None'
            b='Att'
        elif k.find('Detached')!= -1:
            if k.find('Car Garage') != -1:
                parknum=re.sub('\D','',sron(k).finder('Parking:','Car Garage'))
            else:
                parknum='None'
            b='Det'
        elif k.find('Car Garage') != -1:
            b='None'
            parknum=re.sub('\D','',sron(k).finder('Parking:','Car Garage'))
        else:
            b='None'
            parknum='None'
            print('Error in finding Garage type and parking spots')

        d['garage']=b
        try:
            if int(parknum) > 3:
                d['parking spots']='3'
            else:
                d['parking spots']=parknum
        except:
            d['parking spots']=parknum

    def acres():
        k=lsron(raw).finder('Lot Sq Ft:',':')
        b=re.search('\.\d{2}', k)[0] 
        d['acres']=sron(k).finder(': ',b)[2:]

    def public():
        public=lsron(raw).finder('Public:','Showing')[len('Public: '):][0:-len('Showing')]
        d['public']=public
   

def runner(self):
    braw(self)
    global zips
    zips = [elem.strip() for elem in open('zips.csv','r').readlines()[0].split(',') ]
    rist.addressnzip()
    rist.prices()
    rist.DOM()
    rist.dates()
    rist.age()
    rist.floorsnstyle()
    rist.sqft()
    rist.bednbath()
    rist.type()
    rist.garage()
    rist.acres()
    rist.public()
    return d


    

  
