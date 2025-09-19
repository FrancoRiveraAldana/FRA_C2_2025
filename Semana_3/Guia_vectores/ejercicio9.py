# 9. Intercambiar elementos pares por ceros:
# Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
# resultante

lista_1 = [7, 8, 10, 5, 3, 16]

print (f'La lista original {lista_1}')
for i in range (len(lista_1)):
    if  lista_1[i] % 2 == 0:
        lista_1[i] = 0 

print (f'La lista modificada {lista_1}')







