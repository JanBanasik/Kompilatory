class SymbolsList:
    @staticmethod
    def is_plus(token: str) -> bool:
        return token == "+"

    @staticmethod
    def is_minus(token: str) -> bool:
        return token == "-"

    @staticmethod
    def is_multiply(token: str) -> bool:
        return token == "*"

    @staticmethod
    def is_divide(token: str) -> bool:
        return token == "/"

    @staticmethod
    def is_left_parenthesis(token: str) -> bool:
        return token == "("

    @staticmethod
    def is_right_parenthesis(token: str) -> bool:
        return token == ")"

    @staticmethod
    def is_letter(token: str) -> bool:
        return token.isalpha()

    @staticmethod
    def is_dot(token: str) -> bool:
        return token == '.'

    @staticmethod
    def is_digit(token: str) -> bool:
        return token.isdigit()

    @staticmethod
    def is_identifier(token: str) -> bool:
        if not token or not SymbolsList.is_letter(token[0]):
            return False

        return all(SymbolsList.is_letter(c) or SymbolsList.is_digit(c) for c in token[1:])

    @staticmethod
    def scan_digits(token: str, start: int, at_least_one: bool = False) -> tuple[bool, int]:
        index = start
        found_at_least_one = False

        while index < len(token) and SymbolsList.is_digit(token[index]):
            found_at_least_one = True
            index += 1

        if at_least_one and not found_at_least_one:
            return False, start

        return True, index

    @staticmethod
    def is_valid_number(token: str) -> tuple[bool, int]:
        if not token:
            return False, -1

        success, pos = SymbolsList.scan_digits(token, 0, True)
        if not success:
            return False, pos

        if pos == len(token):
            return True, pos

        if token[pos] == ".":
            success, next_pos = SymbolsList.scan_digits(token, pos + 1, True)
            if not success:
                return False, next_pos

            if next_pos == len(token):
                return True, next_pos

            if token[next_pos] not in ['E', 'e']:
                return False, next_pos

            return SymbolsList.tokens_after_e(token, next_pos)

        if token[pos] in ['E', 'e']:
            return SymbolsList.tokens_after_e(token, pos)

        return False, pos

    @staticmethod
    def tokens_after_e(token: str, pos: int) -> tuple[bool, int]:
        next_pos = pos + 1
        if next_pos >= len(token):
            return False, pos

        if not (SymbolsList.is_plus(token[next_pos]) or SymbolsList.is_minus(token[next_pos])):
            return False, next_pos

        next_pos += 1
        success, next_pos = SymbolsList.scan_digits(token, next_pos, True)

        if not success:
            return False, next_pos

        return next_pos == len(token), next_pos

    @staticmethod
    def isToken(token: str) -> bool:
        10.5e-10+4.5


# Przykładowe wywołanie
print(SymbolsList.is_valid_number("10e"))