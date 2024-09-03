from exceptions import ValidationError
from settings import VALIDATION_SUBJECTS, VALIDATION_ERROR_MESSAGE


def number_validator(number: str, length: int, validator_subject: str):
    """Валидатор СМС-кода и номера телефона"""
    if validator_subject not in VALIDATION_SUBJECTS:
        raise ValueError(f'{validator_subject} not in {VALIDATION_SUBJECTS}')
    if len(number) != length:
        raise ValidationError(
            VALIDATION_ERROR_MESSAGE.format(validator_subject=validator_subject)
        )
    for i in number:
        if not i.isdigit():
            raise ValidationError(
                VALIDATION_ERROR_MESSAGE.format(validator_subject=validator_subject)
            )
