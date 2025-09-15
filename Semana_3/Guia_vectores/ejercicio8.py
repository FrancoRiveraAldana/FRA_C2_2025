# 8. Comparar dos arrays:
# Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
# y mostrar un mensaje indicando si son o no iguales

lista_1 = []
for i in range (5):
    peticion = int(input("ingrese un numero para la lista 1: "))
    lista_1.append (peticion)

lista_2 = []
for ii in range (5):
    peticion_2 = int(input("ingrese un numero para la lista 2: "))
    lista_2.append (peticion_2)

print (f'Lista 1 {lista_1}')
print (f'Lista 2 {lista_2}')


if lista_1 == lista_2:
    print ('ambas listas son iguales')
else:
    print ('las listas no son iguales')


