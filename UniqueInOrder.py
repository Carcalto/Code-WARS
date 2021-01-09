
def unique_in_order(palavra):
    
    palavra = list(palavra)
    lista = []
    i = 0

    if len(palavra) == 1:
        lista = palavra

    while i < len(palavra) - 1 and len(palavra) != 1:
   
        if palavra[i] == palavra[i + 1]:
            i += 1
        else:
            lista.append(palavra[i])
            i += 1

        if i == len(palavra) - 1:
            lista.append(palavra[i])



    return lista
        
palavra ='AAAABBBCCDAABBB'

unique_in_order(palavra)