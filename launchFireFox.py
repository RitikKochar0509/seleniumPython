import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#chrome_options = Options()
#chrome_options.add_argument("--disable-exte")
#driver = webdriver.Chrome(executable_path=r"D:\Automation Tools\python\seleniumPython\driver\chromedriver.exe",chrome_options=chrome_options)

driver = webdriver.Firefox(executable_path=r"D:\Automation Tools\python\seleniumPython\driver\gecoV20\geckodriver.exe")



# Navigate to the application home page
driver.get("https://pypi.org/")
driver.implicitly_wait(10)
# get the search textbox

searchfield = driver.find_element_by_xpath(".//*[@id='search']")
print(searchfield)
time.sleep(2)

searchfield.send_keys("selenium")

searchbutton = driver.find_element_by_xpath(".//*[@id='content']/section[1]/div/form/button")

searchbutton.click()
time.sleep(5)
driver.quit()

