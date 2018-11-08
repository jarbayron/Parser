import re
import os
import pandas as pd
import zipfile
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

##shutil.rmtree(r'C:\Users\Bayron\Desktop\Money\43placidln\threeup')
##b=0
##while b==0:
##    try:
##        os.makedirs(r'C:\Users\Bayron\Desktop\Money\43placidln\threeup')
##        b=1
##    except:
##        pass


chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\threeup"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

driver.get('http://www.convertimagetotext.net/imagetotextconverter.php')
driver.find_element_by_xpath('// div [@class="add-file-button"]').click()
##driver.find_element_by_css_selector('input[type="file"]').clear
##uploader=driver.find_element_by_css_selector('input[type="file"]')
##
##uploader.send_keys("C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\email\\3up.pdf")


##while (os.stat('C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\Textfiles\\threeup').st_size)== 0:
##    time.sleep(4)
##    driver.find_element_by_xpath('//select {@id="language"][@id="language"]').send_keys('english')    
##    
##
##if (os.path.exists('C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\Textfiles\\pdftotext.zip')) == True:
##    driver.quit()    
##
##zip_ref=zipfile.ZipFile('C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\Textfiles\\pdftotext.zip','r')
##zip_ref.extractall('C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\Textfiles')
##zip_ref.close()
##
##def data141():
##    b=[]
##    for i in range(0,15):
##        fp=open(os.path.join('C:\\Users\\Bayron\\Desktop\\Money\\43placidln\\Textfiles','document-page%s.txt' % i),'r')
##        lines=fp.readlines()
##        str1=''.join(lines)
##        c=re.sub('\n','',str1)
##        if 'Active$' in c:
##            b.append(i)
##    return b
