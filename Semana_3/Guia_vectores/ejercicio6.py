# 6. Mayor y su posición:
# Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se
# encuentra



lista = [] 

for i in range (7):
    peticion = int(input ("ingrese un numero"))
    lista.append (peticion)

maximo = 0

for i in range (len(lista)):
    if lista[i] > maximo:
        maximo = lista[i]
        posicion = i

print (f'La lista de números es {lista}')
print (f'El número más grande es {maximo} y se encuentra en la posicion {posicion}')

