"""Checks whether or not a given il-id is valid"""

def valid(inp):
    if not (inp.isdigit() and len(inp) == 9):
        return False

    out = list(map(int, inp))
    out[1::2] = map(lambda x: sum(divmod(x * 2, 10)), out[1::2])

    return sum(out) % 10 == 0
