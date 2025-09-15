# Sumar todos los elementos:
# Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los
# elementos


lista = []
total = 0

for i in range (10):
    peticion = int(input ("ingrese un numero"))
    lista.append (peticion)
    total += peticion


print (f"Numeros ingresados {lista}")
print (f"Sumatoria total es {total}")