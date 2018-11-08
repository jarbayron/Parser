import re
import os
import pandas as pd
import zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys




chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\Textfiles"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

driver.get('https://pdftotext.com/')

driver.find_element_by_css_selector('input[type="file"]').clear
uploader=driver.find_element_by_css_selector('input[type="file"]')

for i in range(0,15):
    uploader.send_keys("C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\pdfs\\document-page%s.pdf" % i)


while (os.path.exists('C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\Textfiles\\pdftotext.zip'))== False:
    time.sleep(4)
    driver.find_element_by_xpath('//button [@id="download-all"]').click()    
    

if (os.path.exists('C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\Textfiles\\pdftotext.zip')) == True:
    driver.quit()    

zip_ref=zipfile.ZipFile('C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\Textfiles\\pdftotext.zip','r')
zip_ref.extractall('C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\Textfiles')
zip_ref.close()

def data141():
    b=[]
    for i in range(0,15):
        fp=open(os.path.join('C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\Textfiles','document-page%s.txt' % i),'r')
        lines=fp.readlines()
        str1=''.join(lines)
        c=re.sub('\n','',str1)
        if 'Active$' in c:
            b.append(i)
    return b
        


        


    
