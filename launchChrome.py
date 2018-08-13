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



driver.close()