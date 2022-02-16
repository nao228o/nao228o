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


d = []
for shop_url in shop_urls:
    driver.get(shop_url)

    sleep(2)

    d_list = {}
    d_list['店名'] = None
    d_list['TEL'] = None
    d_list['最寄駅'] = None
    d_list['アクセス'] = None
    d_list['住所'] = None
    d_list['営業時間'] = None
    d_list['定休日'] = None
    d_list['感染症対策'] = None
    d_list['平均予算'] = None
    d_list['クレジット\nカード'] = None
    d_list['その他決済'] = None
    d_list['キャパシティ'] = None
    d_list['席数形態'] = None
    d_list['駐車場'] = None
    d_list['テイクアウト・\nデリバリー'] = None
    d_list['禁煙・喫煙'] = None
    d_list['こだわり'] = None
    d_list['ホームページ'] = None
    d_list['備考'] = None

    shop_info = driver.find_element(By.CLASS_NAME, 'shop_info')
    elems_tr = shop_info.find_elements(By.TAG_NAME, 'tr')

    for elem_tr in elems_tr:
        key = elem_tr.find_element(By.TAG_NAME, 'th')
        value = elem_tr.find_element(By.TAG_NAME, 'td')

        if key.text == '店名':
            d_list['店名'] = value.text
        elif key.text == 'TEL':
            d_list['TEL'] = value.text
        elif key.text == '最寄駅':
            d_list['最寄駅'] = value.text
        elif key.text == 'アクセス':
            d_list['アクセス'] = value.text
        elif key.text == '住所':
            d_list['住所'] = value.text
        elif key.text == '営業時間':
            d_list['営業時間'] = value.text
        elif key.text == '定休日':
            d_list['定休日'] = value.text
        elif key.text == '感染症対策':
            d_list['感染症対策'] = value.text
        elif key.text == '平均予算':
            d_list['平均予算'] = value.text
        elif key.text == 'クレジット\nカード':
            d_list['クレジット\nカード'] = value.text
        elif key.text == 'その他決済':
            d_list['その他決済'] = value.text
        elif key.text == 'キャパシティ':
            d_list['キャパシティ'] = value.text
        elif key.text == '席数形態':
            d_list['席数形態'] = value.text
        elif key.text == '駐車場':
            d_list['駐車場'] = value.text
        elif key.text == 'テイクアウト・\nデリバリー':
            d_list['テイクアウト・\nデリバリー'] = value.text
        elif key.text == '禁煙・喫煙':
            d_list['禁煙・喫煙'] = value.text
        elif key.text == 'こだわり':
            d_list['こだわり'] = value.text
        elif key.text == 'ホームページ':
            d_list['ホームページ'] = value.text
        elif key.text == '備考':
            d_list['備考'] = value.text
        else:
            pass

    d.append(d_list)

    sleep(1)

df = pd.DataFrame(d)
df.head()
df.to_csv("ヒトサラ.csv", index=False)

driver.back()

sleep(5)

driver.quit()