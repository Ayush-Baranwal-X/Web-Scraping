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

cur_n = os.path.basename(__file__)
re_n = input("Enter the name of the Python File('Eg:- name.py') ")
os.rename('./'+cur_n,'./'+re_n) 


PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)


cn = input("Enter Contest No ")

alphas=[]
for i in range(65,91):
    alphas.append(chr(i))
k = 0


for alpha in alphas:
    st = str("https://codeforces.com/problemset/problem/"+str(cn)+"/"+str(alpha))
    driver.maximize_window()
    driver.get(st)
    tl = driver.find_element_by_class_name("title")
    tt = tl.text
    print(tt)
    ver = tt[0]
    if (ver == alphas[k-1]):
        break
    k += 1



    path = "./"+str(cn)+"/"+str(alpha)
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
        f= open("./"+str(cn)+"/"+str(alpha)+"/input"+str(var1)+".txt","w+")
        f.write((ls[num]).text)
        var1 +=1
        f.close()

    for num in range(1,50,2):
        if ((num+1) > len1):
            break        
        f= open("./"+str(cn)+"/"+str(alpha)+"/output"+str(var2)+".txt","w+")
        f.write((ls[num]).text)
        var2 +=1
        f.close()
   


    element1 = driver.find_element_by_class_name('problem-statement')
    element1.screenshot("./"+str(cn)+"/"+str(alpha)+"/problem.png")

driver.close()