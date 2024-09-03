# [Проект tanais.express parser.](https://github.com/QuickLike/tanais_express)

## Описание проекта:

Парсер статуса последнего заказа с сайта таможенной службы [TANAIS.Express](https://tanais.express/).

### Запуск проекта:
Клонируйте [репозиторий](https://github.com/QuickLike/tanais_express) и перейдите в него в командной строке:
```
git clone https://github.com/QuickLike/tanais_express

cd tanais_express
```
Создайте виртуальное окружение и активируйте его

Windows
```
python -m venv venv
venv/Scripts/activate
```

Linux/Ubuntu/MacOS
```
python3 -m venv venv
source venv/bin/activate
```
Обновите pip:
```
python -m pip install --upgrade pip
```
Установите зависимости:
```
pip install -r requirements.txt
```
Также для работы парсера необходим установленный браузер Google Chrome.

(Опционально)Для получения информации о статусе в Telegram, нужно создать файл .env, и добавить переменные:
```
BOT_TOKEN=<токен_вашего_бота>
CHAT_ID=<ваш_id>
```


## Запуск парсера

```
python main.py
```
Откроется окно браузера, его нужно свернуть и вводить все данные в консоль.


## Автор

[Власов Эдуард](https://github.com/QuickLike)
