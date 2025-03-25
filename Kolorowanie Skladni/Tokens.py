KEYWORDS = ["break", "if", "else", "for", "while", "import", "static", "return", "class", "public"]
BOOLEANS = ["true", "false"]
OPERATORS = ["=", "!", "+", "-", "*", "/", "<", ">"]
BRACKETS = ["(", ")", "[", "]", "{", "}"]
TYPES = ["int", "String", "void"]
SPECIALS = [';', ' ', '\n', "\""]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7' '8', '9']



token_colors = {
        'KEYWORDS': 'color: blue; font-weight: bold;',
        'BOOLEANS': 'color: red; font-weight: bold;',
        'TYPES': 'color: green; font-weight: bold;',
        'OPERATORS': 'color: orange;',
    }

automata = {
    0: {'znak': 1,
        'nawias': 3,
        'operator': 5,
        'specjalny': 7,
        'cyfra': 8},

    1: {'znak': 1,
        'cyfra': 1,
        'inne': 2,
        'specjalny': 2},

    3: {'inne': 4,
        'specjalny': 4},

    5: {'inne': 6,
        'specjalny': 6},

    8: {'cyfra': 8,
        'inne': 9,
        'specjalny': 9}
}

stanyKoncowe = {2: 'identyfikator',
                4: 'Nawias',
                6: 'Operator',
                7: 'specjalny',
                9: 'liczba'}


def klasyfikuj(znak: str) -> str:
    if znak.isalpha() or znak == ".":
        return 'znak'
    elif znak in BRACKETS:
        return 'nawias'
    elif znak in SPECIALS:
        return "specjalny"
    elif znak in OPERATORS:
        return 'operator'
    elif znak in NUMBERS:
        return 'cyfra'
    return "inne"


def skaner(expression: str, f) -> tuple[str, str, bool]:
    style = 'color: black;'
    stan = 0
    token: str = ""
    endOfExpr: bool = True
    special = ""
    for index in range(len(expression)):
        klasyfikacja = klasyfikuj(expression[index])
        if klasyfikacja == 'specjalny':
            special = expression[index]
        if klasyfikacja not in automata[stan]:
            klasyfikacja = 'inne'
        stan = automata[stan][klasyfikacja]
        if stan in stanyKoncowe:
            endOfExpr = False
            break
        token += expression[index]

    if endOfExpr:
        stan = automata[stan]['inne']

    if token != "":
        if stanyKoncowe[stan] in ['Nawias', 'liczba']:
            f.write(f'<span style="{style}">{token}</span>')
        elif stanyKoncowe[stan] == 'Operator':
            f.write(f'<span style="{token_colors['OPERATORS']}">{token}</span>')
        else:
            if token in KEYWORDS:
                f.write(f'<span style="{token_colors['KEYWORDS']}">{token}</span>')
            elif token in BOOLEANS:
                f.write(f'<span style="{token_colors['BOOLEANS']}">{token}</span>')
            elif token in TYPES:
                f.write(f'<span style="{token_colors['TYPES']}">{token}</span>')
            else:
                f.write(f'<span style="{style}">{token}</span>')
    if special != "":
        if special == '\n':
            f.write("<br>")
        else:
            f.write(special)

    return stanyKoncowe[stan], token, special != ""


input_text = open("program.txt", "r").read()
f = open("res.html", "wt")
f.write('<html><head><style>body { font-family: monospace; }</style></head><body><pre>')

i = 0
while i < len(input_text):
    typ, wartosc, wasSpecial = skaner(input_text[i:], f)
    i += len(wartosc)
    if wasSpecial:
        i += 1
    print(f"({typ}, {wartosc}) {i=}")

f.write('</pre></body></html>')