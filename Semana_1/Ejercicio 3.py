# 3. Definir una función area_triangulo que reciba la base y la altura de un triángulo y
# devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado.
# Fórmula: area = (b * h) / 2.

def area_triangulo (base:float , altura:float )-> float:
    area = base * altura
    return "El valor del area es = " + str ( area / 2 )

valor_base = int(input('¿Cual es el valor de la base? '))
valor_alt = int (input('Cual es el valor de la altura? '))

print (area_triangulo (valor_base, valor_alt))


       


