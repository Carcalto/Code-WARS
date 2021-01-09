
def DNA_strand(dna):
    
    dna = dna.upper()
    lista = ''

    for char in dna:
        if char == 'A':
            lista += 'T'

        if char == 'T':
            lista += 'A'

        if char == 'C':
            lista += 'G'

        if char == 'G':
            lista += 'C'

    return lista


DNA_strand("attGC")