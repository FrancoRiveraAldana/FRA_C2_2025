# Promedio de valores:
# Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio
# de los valores


lista = [] 
sumatoria = 0
total = 0

for i in range (6):
    peticion = float(input ("ingrese un numero"))
    lista.append (peticion)
    sumatoria += peticion
total = sumatoria / 6


print (f'numeros ingresados {lista}')
print (f'promedio igual {total}')