from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

chrome_path = '/Users/tsushima/Desktop/ScrapingBeginner-main/chromedriver 3'

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)
base_url = "https://hitosara.com/aichi/lst/?page={}"
shop_urls = []
for i in range(1,2):
    target_url = base_url.format(i)

    driver.get(target_url)

    sleep(3)

    elems = driver.find_elements(By.CLASS_NAME, 'shop-info-wrapper')
    
    for elem in elems:
        aTag    = elem.find_element(By.TAG_NAME, 'a')
        url     = aTag.get_attribute('href')
        shop_urls.append(url)
        print("店舗urlの数:",len(shop_urls))
        sleep(1)

d_list = []
for shop_url in shop_urls:
    driver.get(shop_url)

    sleep(2)

    shop_info = driver.find_element(By.CLASS_NAME, 'shop_info')
    elems_th = shop_info.find_elements(By.TAG_NAME, 'th')
    keys = []
    for elem_th in elems_th:
        key = elem_th.text
        keys.append(key)
    print(len(keys))
    print(keys)

    elems_td = shop_info.find_elements(By.TAG_NAME, 'td')
    values = []
    for elem_td in elems_td:
        value = elem_td.text
        values.append(value)
    print(len(values))
    print(values)

    sleep(1)

'''df = pd.DataFrame(d_list)
df['項目'] = keys
df['値'] = values
df.to_csv("ヒトサラ.csv", index=False)'''

driver.back()

sleep(5)

driver.quit()