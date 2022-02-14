from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

chrome_path = '/Users/tsushima/Desktop/ScrapingBeginner-main/chromedriver 3'

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)
base_url = "https://hitosara.com/aichi/lst/"
driver.get(base_url)

sleep(3)

elements = driver.find_elements(By.CLASS_NAME, 'shop-info-wrapper')
element = elements[0]
aTag    = element.find_element(By.TAG_NAME, 'a')
url     = aTag.get_attribute('href')
print('test1 OK!!')

driver.get(url)

sleep(3)

shop_info = driver.find_element(By.CLASS_NAME, 'shop_info')
elems_th = shop_info.find_elements(By.TAG_NAME, 'th')
keys = []
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)
print(keys)

elems_td = shop_info.find_elements(By.TAG_NAME, 'td')
values = []
for elem_td in elems_td:
    value = elem_td.text
    values.append(value)
print(values)

sleep(2)

df = pd.DataFrame()
df['項目'] = keys
df['値'] = values

df.to_csv("ヒトサラ.csv", index=False)

driver.back()

sleep(5)

driver.quit()