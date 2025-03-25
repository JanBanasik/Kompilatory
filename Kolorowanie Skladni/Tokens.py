KEYWORDS = ["if", "else", "for", "while", "import", "static", "return", "class"]
BOOLEANS = ["true", "false"]
OPERATORS = ["=", "!", "+", "-", "*", "/", "<", ">"]
BRACKETS = ["(", ")", "[", "]", "{", "}"]
TYPES = ["int", "String", "void"]
SPECIALS = [';']



token_colors = {
        'KEYWORD': 'color: blue; font-weight: bold;',
        'NUMBER': 'color: green;',
        'STRING': 'color: red;',
        'COMMENT': 'color: gray; font-style: italic;',
        'IDENTIFIER': 'color: black;',
        'OPERATOR': 'color: purple;',
        'PUNCTUATION': 'color: brown;',
        'WHITESPACE': '',
        'NEWLINE': '',
    }

automata = {
    0: {'znak': 1,
        'nawias': 3,
        'operator': 5,
        'specjalny': 7},

    1: {'znak': 1,
        'inne': 2},

    3: {'inne': 4},

    5: {'inne': 6}
}

stanyKoncowe = {2: 'identyfikator',
                4: 'Nawias',
                6: 'Operator',
                7: 'specjalny'}


def klasyfikuj(znak: str) -> str:
    if znak.isalpha() or znak == ".":
        return 'znak'
    elif znak in BRACKETS:
        return 'nawias'
    elif znak in SPECIALS:
        return "specjalny"
    elif znak in OPERATORS:
        return 'operator'
    elif znak == '\n':
        return "nowaLinia"
    elif znak == " ":
        return "spacja"
    return "inne"


def skaner(expression: str, f) -> tuple[str, str]:
    style = 'color: blue; font-weight: bold;'
    stan = 0
    token: str = ""
    endOfExpr: bool = True
    for index in range(len(expression)):
        if expression[index] == "\n":
            f.write(f'<span style="{style}">{token}</span>')
            f.write('<br>')
            return ("chuj", token + "\n")
        elif expression[index].isspace():
            f.write(" ")
        else:
            klasyfikacja = klasyfikuj(expression[index])

            if klasyfikacja not in automata[stan]:
                klasyfikacja = 'inne'
            print(stan, klasyfikacja, token, expression[index])
            stan = automata[stan][klasyfikacja]
            print(stan)
            if stan in stanyKoncowe:
                endOfExpr = False
                break
            token += expression[index]

    if endOfExpr:
        stan = automata[stan]['inne']

    f.write(f'<span style="{style}">{token}</span>')

    return stanyKoncowe[stan], token


input_text = open("program.txt", "r").read()
f = open("res.html", "wt")
f.write('<html><head><style>body { font-family: monospace; }</style></head><body><pre>')

i = 0
while i < len(input_text):
    typ, wartosc = skaner(input_text[i:], f)
    i += len(wartosc)
    print(f"({typ}, {wartosc}) {i=}")
