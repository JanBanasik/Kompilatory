from liczbaBZ import match_number


class Token:
    def __init__(self, type, value, position):
        self.type = type
        self.value = value
        self.position = position

    def __repr__(self):
        return f"({self.type}, {self.value})"


def is_digit(char):
    return char in '0123456789'


def is_letter(char):
    return char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def is_whitespace(char):
    return char in ' \t\n'


def scan_expression(expression):
    tokens = []
    i = 0
    n = len(expression)

    while i < n:
        if is_whitespace(expression[i]):
            i += 1
            continue

        if is_digit(expression[i]):
            start = i
            lastValueBZ = i  # position of last 2
            # 2 -> 0 - zapisz bz
            # 1 -> 0 chuj
            #
            while i < n:
                res = match_number(expression[start:i + 1])
                print(expression[start:i+1], res)
                if res == 0:
                    break
                elif res == 2:
                    lastValueBZ = i
                i += 1

            i = lastValueBZ + 1
            tokens.append(Token('Liczba', expression[start:lastValueBZ + 1], start))
            continue

        if is_letter(expression[i]):
            start = i
            while i < n and (is_letter(expression[i]) or is_digit(expression[i])):
                i += 1
            tokens.append(Token('Identyfikator', expression[start:i], start))
            continue

        if expression[i] == '+':
            tokens.append(Token('Plus', '+', i))
            i += 1
            continue

        if expression[i] == '-':
            tokens.append(Token('Minus', '-', i))
            i += 1
            continue

        if expression[i] == '*':
            tokens.append(Token('Razy', '*', i))
            i += 1
            continue

        if expression[i] == '/':
            tokens.append(Token('Dziel', '/', i))
            i += 1
            continue

        if expression[i] == '(':
            tokens.append(Token('LNaw', '(', i))
            i += 1
            continue

        if expression[i] == ')':
            tokens.append(Token('PNaw', ')', i))
            i += 1
            continue

        # Obsługa błędów
        print(f"Błąd: Nieznany znak '{expression[i]}' na pozycji {i}")
        i += 1

    return tokens


# Przykład użycia
expression = "25.3e10+3*(76+8/3)+ 3*(9-3)"
tokens = scan_expression(expression)
for token in tokens:
    print(token)
