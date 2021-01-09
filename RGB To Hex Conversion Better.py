
def rgb(r, g, b):

    lista = [r, g, b]
    resultado = ''

    for char in lista:
        if char < 0:
            resultado += format(0, '02X')
        elif char > 255:
             resultado += format(255, '02X')
        else:
             resultado += format(char, '02X')


    return resultado


rgb(1,2,3)