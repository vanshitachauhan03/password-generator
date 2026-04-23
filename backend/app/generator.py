import secrets
import string

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{}|;:,.<>?"
AMBIGUOUS = set("0Ol1I")


def generate_password(length=16, use_uppercase=True, use_lowercase=True,
                      use_digits=True, use_symbols=True,
                      exclude_ambiguous=False, no_repeats=False):

    pool = ""
    required = []

    if use_uppercase:
        pool += UPPERCASE
        required.append(secrets.choice(UPPERCASE))

    if use_lowercase:
        pool += LOWERCASE
        required.append(secrets.choice(LOWERCASE))

    if use_digits:
        pool += DIGITS
        required.append(secrets.choice(DIGITS))

    if use_symbols:
        pool += SYMBOLS
        required.append(secrets.choice(SYMBOLS))

    if not pool:
        raise ValueError("Select at least one character set")

    if exclude_ambiguous:
        pool = "".join(c for c in pool if c not in AMBIGUOUS)

    chars = required[:]

    while len(chars) < length:
        chars.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(chars)

    return "".join(chars)