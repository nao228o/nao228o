from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_path = "/Users/tsushima/Desktop/ScrapingBeginner-main/chromedriver 3"

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)
driver.get('https://hitosara.com/aichi/lst/')

sleep(3)

element = driver.find_element_by_class_name('shop-info-wrapper')
aTag    = element.find_element_by_tag_name("a")
url     = aTag.get_attribute("href")
print("test1 OK!!")

driver2 = driver.get(url)

sleep(3)

elems_th = driver2.find_elements_gy_tag_name('th')
keys = []
for i,elem_th in elems_th:
    if elem_th[i] == None:
        elem_th[i] == elem_th[i]
    else :
        key = elem_th.text
    keys.append[key]

print(keys)

elems_td = driver2.find_elements_gy_tag_name('td')
values = []
for i,elem_td in elems_td:
    if elem_td[i] == None:
        elem_td[i] == elem_td[i]
    else:
        value = elem_td.text
    values.append[value]

print(values)
driver.back()

sleep(2)

driver.quit()