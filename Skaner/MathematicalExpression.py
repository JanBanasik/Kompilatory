automata = {
    0: {'cyfra': 1,
        'nawias': 3,
        'operator': 5},

    1: {'cyfra': 1,
        'inne': 2},

    3: {'inne': 4},

    5: {'inne': 6}
}

stanyKoncowe = {2: 'LiczbaCalkowita',
                4: 'Nawias',
                6: 'Operator'}


def klasyfikuj(znak: str) -> str:
    if znak.isdigit():
        return 'cyfra'
    elif znak in ['(', ')']:
        return 'nawias'
    elif znak in ['+', '-', '*', '/']:
        return 'operator'
    return 'inne'


def skaner(expression: str) -> tuple[str, str]:
    stan = 0
    token: str = ""
    endOfExpr: bool = True
    for index in range(len(expression)):
        if expression[index].isspace():
            continue
        klasyfikacja = klasyfikuj(expression[index])
        if klasyfikacja not in automata[stan]:
            klasyfikacja = 'inne'
        stan = automata[stan][klasyfikacja]
        if stan in stanyKoncowe:
            endOfExpr = False
            break
        token += expression[index]

    if endOfExpr:
        stan = automata[stan]['inne']
    return stanyKoncowe[stan], token


input_text = "2+3*(76+8/3)+ 3*(9-3)"

i = 0
while i < len(input_text):
    typ, wartosc = skaner(input_text[i:])
    i += len(wartosc)
    print(f"({typ}, {wartosc}) {i=}")
