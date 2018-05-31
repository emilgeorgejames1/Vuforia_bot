import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


CHROME_PATH = '/Applications/Google Chrome.app'
CHROMEDRIVER_PATH = 'data/chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
#chrome_options.binary_location = CHROME_PATH

useremailStr = "YOUR_EMAIL_ID_HERE"
passwordStr = "YOUR_PASSWORD_HERE"

browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                         )
# browser = webdriver.Chrome('/Users/mac/Downloads/chromedriver')
browser.get(('https://developer.vuforia.com/vui/auth/login'))

# fill in email and hit the next button

useremail = browser.find_element_by_id('login_email')
useremail.send_keys(useremailStr)
userpassword = browser.find_element_by_id('login_password')
userpassword.send_keys(passwordStr)

signInButton = browser.find_element_by_id('login')
signInButton.click()
time.sleep(2)
browser.find_element_by_id("targetManagerUrl").click()
time.sleep(2)
browser.find_elements_by_class_name("projectNameDisplay")[0].click();
time.sleep(2)
browser.find_element_by_id('addDeviceTargetUserView').click()
time.sleep(2)

# fill add target fields

file = 'PATH_TO_IMAGE_FILE' 
filewidth = 320
filename = 'IMAGE_NAME'

uploadfile = browser.find_element_by_id('targetImgFile')
uploadfile.send_keys("/Users/mac/Desktop/hhh.png")
width = browser.find_element_by_id('targetDimension')
width.send_keys(filewidth)
name = browser.find_element_by_id('targetName')
name.send_keys(filename)
browser.find_element_by_id('AddDeviceTargetBtn').click()
print 'done' 

