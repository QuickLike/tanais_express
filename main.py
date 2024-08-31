import logging
import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from validators import number_validator


MAIN_URL = 'https://tanais.express/?auth'


def authorize(browser):
    field = browser.find_element(By.ID, 'phoneNumber')
    phone_number = input('Введите номер телефона: ')
    if not number_validator(phone_number, 10):
        logging.error('Некорректный номер телефона. Завершение работы парсера.')
        return
    field.send_keys(phone_number)
    field.submit()
    browser.implicitly_wait(10)

    field = browser.find_element(By.ID, 'userCode')
    sms_code = input(f'Введите код, отправленный на номер {phone_number}: ')
    if not number_validator(sms_code, 6):
        logging.error('Некорректный СМС-код. Завершение работы парсера.')
        return
    field.send_keys(sms_code)
    field.submit()
    browser.implicitly_wait(10)


def check_status(browser):
    try:
        browser.find_element(By.XPATH, '//*[@id="ul_catalog_menu_LkGdQn"]/li[4]/a').click()
        browser.implicitly_wait(10)
        browser.find_elements(By.CLASS_NAME, 'fa-info-circle')[-1].click()
        browser.implicitly_wait(10)
        statuses = browser.find_element(By.ID, 'swal2-content')
        actual_status = statuses.find_elements(By.TAG_NAME, 'tr')[-1].text
        return actual_status
    except Exception as e:
        logging.exception(e, exc_info=True)


def parse():
    browser = webdriver.Chrome()
    browser.get(MAIN_URL)
    browser.maximize_window()
    browser.implicitly_wait(10)

    authorize(browser)

    old_status = ''
    while True:
        status = check_status(browser)
        if status:
            if status != old_status:
                old_status = status
                logging.info(status)
            browser.refresh()
        sleep(10)


def main():
    parse()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format=('%(asctime)s, '
                '%(levelname)s, '
                '%(funcName)s, '
                '%(lineno)d, '
                '%(message)s'
                ),
        encoding='UTF-8',
        handlers=[logging.FileHandler(__file__ + '.log'),
                  logging.StreamHandler(sys.stdout)]
    )
    main()
