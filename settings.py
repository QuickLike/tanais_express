from environs import Env


env = Env()
env.read_env()


MAIN_URL = 'https://tanais.express/?auth'

BOT_TOKEN = env.str('BOT_TOKEN')
CHAT_ID = env.int('CHAT_ID')

LOG_FORMAT = (
    '%(asctime)s, '
    '%(levelname)s, '
    '%(funcName)s, '
    '%(lineno)d, '
    '%(message)s'
)

PHONE_NUMBER_LENGTH = 10
SMS_CODE_LENGTH = 6

VALIDATION_ERROR_MESSAGE = 'Некорректный {validator_subject}. Завершение работы парсера.'
VALIDATION_SUBJECTS = ('номер телефона', 'СМС-код')

REFRESH_TIME = {
    'MIN': 5,
    'MAX': 60 * 19
}

EXIT_CODE = '0'
