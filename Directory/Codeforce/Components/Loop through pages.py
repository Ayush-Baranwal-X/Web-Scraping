from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


alphas=[]
for i in range(65,91):
    alphas.append(chr(i))
k = 0
for alpha in alphas:
    st = str("https://codeforces.com/problemset/problem/1468/"+str(alpha))
    driver.get(st)
    tl = driver.find_element_by_class_name("title")
    tt = tl.text
    print(tt)
    ver = tt[0]
    if (ver == alphas[k-1]):
        break
    k += 1
