# 4. Contar mayores a un valor:
# # Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado


lista = [] 
mayor_a_100 = 0

for i in range (8):
    peticion = float(input ("ingrese un numero"))
    lista.append (peticion)

for i in lista:
    if i > 100:
        mayor_a_100 += 1

print (f'lista de 8 {lista}') 
print (f'hay {mayor_a_100} números mayores a 100 ')
    