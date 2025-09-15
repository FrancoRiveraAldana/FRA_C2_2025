# 7. Invertir orden:
# Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero



lista = [] 

for i in range (10):
    peticion = int(input ("ingrese un numero"))
    lista.append (peticion)

inversion_slice = lista[::-1]

print (f'Lista original {lista}')
print (f'lista invertida {inversion_slice}')


