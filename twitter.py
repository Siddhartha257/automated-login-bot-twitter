from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys

email = input("enter your email id")
password = input("enter your password")
username =input("enter your username")

if '@gmail.com' not in email:
    print("enter a valid email id")
    sys.exit(0)
    
url = "https://x.com/i/flow/login"
driver = webdriver.Chrome()
driver.get(url)
actions = ActionChains(driver)
wait = WebDriverWait(driver,10)


# selects the filed of email and submits the required address
element = wait.until(EC.presence_of_element_located((By.NAME,"text")))
element.send_keys(email)
button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.//span[text()='Next']]")))
button.click()


# if there is an verification
verify = wait.until(EC.presence_of_element_located((By.NAME,"text")))
if verify:
    verify.send_keys(username)
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
    next_button.click()


# selects the field of password and submits the required password
try:
    passw = wait.until(EC.presence_of_element_located((By.NAME,"password")))
    passw.send_keys(password)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']")))
    login_button.click()
except:
     print("invalid username")

# stores the divisions of the trending topics
try:
    list = []
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[data-testid='trend']")))
    list = driver.find_elements(By.CSS_SELECTOR,"div[data-testid='trend']")
except:
    print("invalid password")

# for each division in list it fetch the trending topic name and appends to the trends list
trends =[]
for element in list:
    try:
        main = element.find_elements(By.CSS_SELECTOR,"div[dir='ltr']")
        if len(main)>1:
            trend_div = main[1] #in the division of trending topic, title is in second line .. so [1] is used
            trend_topic = trend_div.find_element(By.CSS_SELECTOR, "span").text
            trends.append(trend_topic)

    except:
        print("Error retrieving text from trend element:")
        
# prints the trending topics
print("trending topics in twitter....".upper())
for trend in trends:
    print(trend)

# function to logout the account
def logout_twitter():
    logout = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[data-testid='UserAvatar-Container-SaiSiddhar35056']")))
    logout.click()
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/logout']")))
    element.click()
    enter = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-testid='confirmationSheetConfirm']")))
    enter.click()

time.sleep(3)
time.sleep(5)
logout_twitter()