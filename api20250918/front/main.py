from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument('--headless')
# options.add_argument('--incognito')
# options.add_argument('--window-size=1920x1080')
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)
# driver = webdriver.Firefox()
# driver = webdriver.Edge()
# driver = webdriver.Safari()
driver.get("http://www.codebrainers.pl")
driver.save_screenshot('test.png')
site_title = driver.title
print(f"Tytuł strony to: {site_title}")
assert site_title == 'Coś więcej niż kodowanie - codebrainers'
sleep(20)
driver.quit()