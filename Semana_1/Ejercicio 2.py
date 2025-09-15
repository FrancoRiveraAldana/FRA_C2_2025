# 2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma,
# resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la
# función.


def operaciones (num1:int, num2:int)-> int:
    suma = num1 + num2 
    resta = num1 - num2
    multiplicaciones = num1 * num2
    return "suma = " + str(suma) , " resta = " + str(resta) , "multiplicacion = " + str(multiplicaciones)

numer1 = int(input('Cuál es el primer número? '))
numer2 = int(input ('Cuál es el segundo número? '))

print (operaciones (numer1, numer2))








