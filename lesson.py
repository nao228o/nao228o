from time import sleep

from selenium import webdriver
from selenium.webdriver.options import Options

chrome_path = "/Users/tsushima/Desktop/ScrapingBeginner-main/chromedriver 3"

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)

url = "https://search.yahoo.co.jp/image"
driver.get(url)

sleep(3)

query = 'プログラミンング'
search_box = driver.find_element_by_class_name('SearchBox__searchInput')
search_box.send_keys(query)
search_box.submit()

sleep(3)

driver.quit()