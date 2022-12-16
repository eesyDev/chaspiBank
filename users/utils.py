from django.forms import ValidationError


def validate_cash(cash: float):
    if cash < 1000:
        raise ValidationError('Минимальная сумма 1000 тг')
