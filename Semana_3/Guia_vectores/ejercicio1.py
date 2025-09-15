# 1. Cargar y mostrar array:
# Declarar un array de 5 enteros. Cargarlo por teclado y mostrar su contenido por pantalla usando un
# ciclo for

lista = []

for i in range (5):
    peticion = int(input ("ingrese un numero"))
    lista.append (peticion)

print (lista)