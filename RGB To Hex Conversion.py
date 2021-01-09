
def rgb(r, g, b):

    lista = [r, g, b]

    resultado = ''

    for element in lista:
        if 0 < element <= 255 and len(hex(element)) > 3 :
            resultado += hex(element)[2:]
        elif element == 0:
             resultado += (hex(element)[2:]) * 2
        elif element > 255:
            resultado += 'FF'
        elif element < 0:
            resultado += '00'
        elif len(hex(element)) < 4:
            resultado += '0' + hex(element)[2:]

    return resultado.upper()


print(rgb(-20,275,125))
print(rgb(255,255,255))
print(rgb(1,2,3))


