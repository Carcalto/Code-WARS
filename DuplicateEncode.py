from collections import Counter

def DuplicateEncode(palavra):
    palavra = palavra.lower()
    palavra = list(palavra)
    count = Counter(palavra)
    resultado = ''

    for letra in palavra:
        if count[letra] == 1:
            resultado += '('
    
        else:
            resultado += ')'

    return resultado


DuplicateEncode('recede')

