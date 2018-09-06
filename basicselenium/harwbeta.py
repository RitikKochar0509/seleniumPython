import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

##chrome_options = Options()
#chrome_options.add_argument("--disable-exte")
#driver = webdriver.Chrome(executable_path=r"D:\Automation Tools\python\seleniumPython\driver\chromedriver.exe",chrome_options=chrome_options)

driver = webdriver.Firefox(executable_path=r"D:\Automation Tools\python\seleniumPython\driver\gecoV20\geckodriver.exe")



# Navigate to the application home page
driver.get("http://www.editorialmanager.com/harwbeta150/default.aspx")
driver.implicitly_wait(5)

#Switch to Frame
driver.switch_to.frame(driver.find_element_by_name("content"))
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

#print(driver)
# fill user name and password

username= driver.find_element_by_id("username")
username.send_keys("amyharw")
password = driver.find_element_by_name("password")
password.send_keys("amy123")
authorlogin = driver.find_element_by_name("authorLogin")
authorlogin.click()


# Next window

driver.switch_to.default_content()


time.sleep(10)


driver.find_element_by_xpath(".//*[@id='tableContainer']/div/a[1]").click()

#time.sleep(10)
#driver.quit()

