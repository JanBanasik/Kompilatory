def is_digit(char):
    return char in '0123456789'


def is_exponent_char(char):
    return char in 'Ee'


def is_sign_char(char):
    return char in '+-'


def match_number(s):
    n = len(s)
    i = 0

    # Sprawdzanie części całkowitej
    if i >= n or not is_digit(s[i]):
        return 0
    while i < n and is_digit(s[i]):
        i += 1

    # Sprawdzanie części ułamkowej
    if i < n and s[i] == '.':
        i += 1
        if i >= n:
            return 1
        if not is_digit(s[i]):
            return 0
        while i < n and is_digit(s[i]):
            i += 1

    # Sprawdzanie części wykładniczej
    if i < n:
        if is_exponent_char(s[i]):
            i += 1
            if i < n:
                if is_sign_char(s[i]):
                    i += 1
                    if i >= n:
                        return 1
                    if not is_digit(s[i]):
                        return 0
                    while i < n and is_digit(s[i]):
                        i += 1
                    if i >= n:
                        return 2
                    return 0
                else:
                    return 0
            else:
                return 1
        else:
            return 0
    else:
        return 2
