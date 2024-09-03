import asyncio
import logging
import sys
from time import sleep

from aiogram import Bot
from selenium import webdriver
from selenium.webdriver.common.by import By

from exceptions import ParserError, ValidationError
from settings import (
    BOT_TOKEN,
    MAIN_URL,
    CHAT_ID,
    LOG_FORMAT,
    PHONE_NUMBER_LENGTH,
    REFRESH_TIME,
    SMS_CODE_LENGTH,
    EXIT_CODE
)
from validators import number_validator


if BOT_TOKEN is not None:
    bot = Bot(BOT_TOKEN)


async def authorize(browser):
    field = browser.find_element(By.ID, 'phoneNumber')
    while True:
        phone_number = input('Введите номер телефона: ')
        if phone_number == EXIT_CODE:
            sys.exit('Завершение работы парсера.')
        try:
            number_validator(phone_number, PHONE_NUMBER_LENGTH, 'номер телефона')
        except ValidationError as e:
            logging.exception(e)
            return
        field.send_keys(phone_number)
        field.submit()
        await asyncio.sleep(0.5)
        if 'Пользователь не найден' in browser.page_source:
            print('Пользователь не найден.')
            field.clear()
            continue
        break
    browser.implicitly_wait(10)

    field = browser.find_element(By.ID, 'userCode')
    while True:
        sms_code = input(f'Введите код, отправленный на номер {phone_number}: ')
        if sms_code == EXIT_CODE:
            sys.exit('Завершение работы парсера.')
        try:
            number_validator(sms_code, SMS_CODE_LENGTH, 'СМС-код')
        except ValidationError as e:
            logging.exception(e)
            return
        field.send_keys(sms_code)
        field.submit()
        await asyncio.sleep(0.5)
        if 'Введен неверный код' in browser.page_source:
            print('Введен неверный код.')
            field.clear()
            continue
        break
    browser.implicitly_wait(10)
    logging.info('Успешная авторизация!')
    return True


async def check_status(browser):
    try:
        browser.find_element(By.XPATH, '//*[@id="ul_catalog_menu_LkGdQn"]/li[4]/a').click()
        browser.implicitly_wait(10)
        browser.find_elements(By.CLASS_NAME, 'fa-info-circle')[-1].click()
        browser.implicitly_wait(10)
        statuses = browser.find_element(By.ID, 'swal2-content')
        actual_status = statuses.find_elements(By.TAG_NAME, 'tr')[-1].text
        return actual_status
    except Exception as e:
        raise ParserError(e)


async def parse():
    browser = webdriver.Chrome()
    browser.get(MAIN_URL)
    browser.maximize_window()
    browser.implicitly_wait(10)

    if await authorize(browser) is None:
        return
    while True:
        refresh_time = input(
            'Установите время обновления страницы в секундах.\n'
            f'От {REFRESH_TIME["MIN"]} сек. до {REFRESH_TIME["MAX"]} сек.\n'
        )
        try:
            int(refresh_time)
        except ValueError as e:
            logging.exception(e)
            continue
        if not (REFRESH_TIME["MIN"] <= int(refresh_time) <= REFRESH_TIME["MAX"]):
            print('Неверное значение.')
            continue
        break

    old_status = ''
    while True:
        try:
            status = await check_status(browser)
        except ParserError as e:
            logging.error(e, exc_info=True)
            return
        if status:
            if status != old_status:
                old_status = status
                logging.info(status)
                if BOT_TOKEN is not None:
                    await bot.send_message(CHAT_ID, status)
            browser.refresh()
        sleep(int(refresh_time))


async def main():
    await parse()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        encoding='UTF-8',
        handlers=[logging.FileHandler(__file__ + '.log'),
                  logging.StreamHandler(sys.stdout)]
    )
    asyncio.run(main())
