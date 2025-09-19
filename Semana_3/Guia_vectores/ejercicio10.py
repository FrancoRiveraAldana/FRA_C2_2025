# 10. Función para buscar la primera aparición de un valor:
# Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar
# la posición de la primera aparición de ese número o -1 si no se encuentra


lista = [1, 6, 8, 9]


def busca_valor (lista:list , valor:int )->int:
    for i in range(len(lista)):
        if lista[i] == valor:
            return (f'El número {valor} se encuentra en la posición {i}')
    return (f'-1 , el número {valor} no se encontró')

resultado = busca_valor (lista , 3)
print (resultado)
resultado = busca_valor (lista , 8)
print (resultado)













