from decimal import Decimal
from typing import Optional


def decimal_to_str(decimal_number: Decimal, scale: int = 2) -> Optional[str]:
    if decimal_number is None:
        return
    if scale == 2:
        decimal_str = '{:.2f}'.format(decimal_number)
    else:
        decimal_str = '{:.3f}'.format(decimal_number)

    return decimal_str
