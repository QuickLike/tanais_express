from time import sleep

from requests import Session

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://tanais.express/?auth')
browser.maximize_window()
browser.implicitly_wait(10)
field = browser.find_element(By.ID, 'phoneNumber')
field.send_keys('9775834855')
field.submit()
browser.implicitly_wait(10)
field = browser.find_element(By.ID, 'userCode')
sms_code = input('Enter sms code: ')
field.send_keys(sms_code)
field.submit()
browser.implicitly_wait(10)
browser.find_element(By.XPATH, '//*[@id="ul_catalog_menu_LkGdQn"]/li[4]/a').click()
browser.implicitly_wait(10)
browser.find_element(By.CLASS_NAME, 'fa-info-circle').click()
browser.implicitly_wait(10)
sleep(5)

# session = Session()
# URL = 'https://tanais.express/?auth/'
# data = {
#     'phoneNumber': '9775834855',
#     'method': 'checkLogin',
#     'engine': 'User'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'
# }
# r = session.post(URL, data, headers=headers)
# print(r.status_code)
# with open('index.html', 'w') as f:
#     f.write(r.text)
