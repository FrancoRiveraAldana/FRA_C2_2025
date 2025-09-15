# 5. Buscar un valor:
# Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array.
# Informar la posición en caso afirmativo, o indicar que no se encuentra



lista = [] 

for i in range (10):
    peticion = float(input ('ingrese un numero'))
    lista.append (peticion)
numero = float(input('Indique el numero que busca dentro de la lista'))

for ii in lista:
    if ii == numero:
        for iii in range (len(lista)):
            if lista[iii] == numero:
                print (f'La lista de numeros es {lista}')
                print (f'y el numero {numero} se encuentra en la posicion {iii}')
                break
    else:
        print (f'La lista de numeros es {lista}')
        print ("no se encuentra en esta lista")
        break

