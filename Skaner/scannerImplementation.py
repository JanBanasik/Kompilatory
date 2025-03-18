from tokenList import SymbolsList

class Token:
    def __init__(self, nazwa, wartosc):
        self.nazwa = nazwa
        self.wartosc = wartosc

    def __repr__(self):
        return f"{self.nazwa}: {self.wartosc}"


tokens = set([])

def skaner(text: str) -> Token:
    currentToken = ""
    index = 0
    for i in range(len(text)):
        if isToken(currentToken + text[i]):

    text = text[i:]
    return Token(expr[0], expr[1:])


expr = "254+3*(76+8/3)+ 3*(9-3)"
length = 0
while expr:
    success, token = skaner(expr)

    if not success:
        print(f"Error at {}")
    print(f"Got token {token}")
    length += len(token)
i = 1
while (i < len(expr)):
    success, token = skaner(expr[:i])
    if success:
        i += 1
        while success:
            success, token = skaner(expr[:i])
