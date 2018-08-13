from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-exte")
driver = webdriver.Chrome(executable_path=r"D:\Automation Tools\python\seleniumPython\driver\chromedriver.exe",chrome_options=chrome_options)
#driver = webdriver.Firefox("D:\Automation Tools\python\seleniumPython\driver\geckodriver.exe")
driver.get("http://www.python.org")
assert "Python" in driver.title

print(driver.title)
"""
driver.implicitly_wait(5)
driver.maximize_window()
driver.delete_all_cookies()

elem = driver.find_element_by_name("q")
elem.clear()
print("element found q " );
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source



#D:\Automation Tools\python\seleniumPython\driver\geckodriver.exe

"""
driver.close()