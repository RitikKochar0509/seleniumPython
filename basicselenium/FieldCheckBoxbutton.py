import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select


#chrome_options = Options()
#chrome_options.add_argument("--disable-exte")
#driver = webdriver.Chrome(executable_path=r"D:\Automation Tools\python\seleniumPython\driver\chromedriver.exe",chrome_options=chrome_options)

driver = webdriver.Firefox(executable_path=r"D:\Automation Tools\python\seleniumPython\driver\gecoV20\geckodriver.exe")



# Navigate to the application home page
driver.get("http://demoqa.com")
driver.implicitly_wait(10)
# get the search textbox


registrationlink = driver.find_element_by_xpath(".//*[@id='menu-item-374']/a")
#WebDriverWait(driver,10).until( expected_conditions.element_to_be_clickable(registrationlink))
registrationlink.click()

time.sleep(5)
fname = driver.find_element_by_id("name_3_firstname")
lname = driver.find_element_by_id("name_3_lastname")
maritalStatus = driver.find_element_by_xpath(".//*[@id='pie_register']/li[2]/div/div/input[1]")
hobby = driver.find_element_by_xpath(".//*[@id='pie_register']/li[3]/div/div/input[2]")

fname.send_keys("Aman")
lname.send_keys("Josh")
maritalStatus.click()
hobby.click()


#select list

country = driver.find_element_by_xpath(".//*[@id='dropdown_7']")
selectlist = Select(country)
selectlist.select_by_visible_text("India")
#selectlist.select_by_visible_text("India")
#selectlist.deselect_by_visible_text("India")

selectMonth = Select(driver.find_element_by_xpath(".//*[@id='mm_date_8']"))
selectMonth.select_by_value("1")

selectday = Select(driver.find_element_by_xpath(".//*[@id='dd_date_8']"))
selectday.select_by_index("1")

selectyear = Select(driver.find_element_by_xpath(".//*[@id='yy_date_8']"))
selectyear.select_by_visible_text("2014")

phoneNumber = driver.find_element_by_xpath(".//*[@id='phone_9']")
phoneNumber.send_keys("0038278321")

driver.find_element_by_xpath(".//*[@id='username']").send_keys("username")
driver.find_element_by_xpath(".//*[@id='email_1']").send_keys("abc@gmail.com")






time.sleep(5)
driver.quit()

