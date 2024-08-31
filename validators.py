def number_validator(number: str, length: int) -> bool:
    """Валидатор СМС-кода и номера телефона"""
    if len(number) != length:
        return False
    for i in number:
        if not i.isdigit():
            return False
    return True
