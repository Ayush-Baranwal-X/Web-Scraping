from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://moodle.iitd.ac.in/login/index.php")

a = driver.find_element_by_id("login")

q = driver.find_element_by_id("valuepkg3")



def convert(lst): 
    return (lst[0].split()) 
  
# Driver code 
lst =  [a.text] 
var = convert(lst)
print(var) 

x = var[7]
print(x)

if (x == "enter"):
    y = var[8]
    z =int(var[12])
    k =int(var[10])
    if (y == "first"):
    	q.send_keys(str(k))
    else:
    	q.send_keys(str(z))

elif (x== "add"):
    y = int(var[8])
    z = int(var[10])
    q.send_keys(str(z+y))

elif (x== "subtract"):
    y = int(var[8])
    z = int(var[10])
    f = str(y-z)
    q.send_keys(f)


driver.execute_script("var a = prompt('Enter Username(And just wait for next Dialog box)', 'Username');document.body.setAttribute('data-id', a)")
time.sleep(7)
un1 = driver.find_element_by_tag_name('body').get_attribute('data-id')
un = driver.find_element_by_id("username")

driver.execute_script("var a = prompt('Enter Password(And wait for login)', 'Password');document.body.setAttribute('data-id', a)")
time.sleep(7) 
pw1 = driver.find_element_by_tag_name('body').get_attribute('data-id')
pw = driver.find_element_by_id("password")

un.send_keys(un1)
pw.send_keys(pw1)

log = driver.find_element_by_id("loginbtn")
log.send_keys(Keys.RETURN)










