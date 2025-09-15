# 9. Intercambiar elementos pares por ceros:
# Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
# resultante

lista_1 = []
for i in range (10):
    peticion = int(input("ingrese 10 numeros"))
    lista_1.append (peticion)

for i in lista_1:
    if i % 2 == 0:
        i = 0

print (f'{lista_1}')



