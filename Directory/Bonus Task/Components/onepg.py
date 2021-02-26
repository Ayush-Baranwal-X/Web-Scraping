from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from PIL import Image
from selenium.webdriver.chrome.options import Options


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.maximize_window()

driver.get("https://www.codeforces.com/problemset/problem/1468/C")



path = "./1468/A/"
try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)



in1 = 0
ou1 = 0


ls = driver.find_elements_by_tag_name("pre")
len1 = len(ls)





var1 = 1
var2 = 1

for num in range(0,50,2):
    if ((num+1) > len1):
        break        
    f= open("./1468/A/input"+str(var1)+".txt","w+")
    f.write((ls[num]).text)
    var1 +=1
    f.close()

for num in range(1,50,2):
    if ((num+1) > len1):
        break        
    f= open("./1468/A/output"+str(var2)+".txt","w+")
    f.write((ls[num]).text)
    var2 +=1
    f.close()
time.sleep(3)



#obtain browser height and width
w = driver.execute_script('return document.body.parentNode.scrollWidth')
h = driver.execute_script('return document.body.parentNode.scrollHeight')
#set to new window size
driver.set_window_size(w, h)
#obtain screenshot of page within body tag
driver.find_element_by_class_name('problem-statement').screenshot("./1468/A/problem.png")















