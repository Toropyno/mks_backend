from decimal import Decimal


def decimal_to_str(decimal_number: Decimal) -> str:
    return '{:.2f}'.format(decimal_number)
