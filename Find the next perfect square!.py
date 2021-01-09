import math

def find_next_square(sq):

    if sq % math.sqrt(sq) == 0:
        resultado = (math.sqrt(sq) + 1) ** 2
        return int(resultado)
    else:
        return -1

find_next_square(114)