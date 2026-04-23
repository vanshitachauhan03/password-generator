import math
from .generator import UPPERCASE, LOWERCASE, DIGITS, SYMBOLS


def calculate_entropy(password):
    pool_size = 0

    if any(c in UPPERCASE for c in password):
        pool_size += 26
    if any(c in LOWERCASE for c in password):
        pool_size += 26
    if any(c in DIGITS for c in password):
        pool_size += 10
    if any(c in SYMBOLS for c in password):
        pool_size += len(SYMBOLS)

    if pool_size == 0:
        return 0

    return len(password) * math.log2(pool_size)


def strength_label(entropy):
    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Fair"
    elif entropy < 80:
        return "Strong"
    else:
        return "Very Strong"