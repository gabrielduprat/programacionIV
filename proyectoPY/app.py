#importar tabla

from tabla import tabla_multiplicar
entrada=input("Ingrese un numero: ")
if entrada.isdigit():
    numero=int(entrada)
    tabla_multiplicar(numero)
else:
    print("El numero ingresado no es un numero")

import random
print("Numero aleatorio")
num= random.randint(1,100)
print(num)

from tabla import tabla_multiplicar_aleatorio
print("Numero aleatorio")
print(num)
tabla_multiplicar_aleatorio(num)

from herramientas import contar_palabras
texto="Este es un texto"
print(contar_palabras(texto))

from herramientas import invertir
texto="Este es un texto"
print(invertir(texto))

from herramientas import palabras_comienza_con
texto="este es un texto"
print(palabras_comienza_con(texto,"e"))

from herramientas import contar_palabras_repetidas
texto="Este es un texto asd asd"
print(contar_palabras_repetidas(texto)) 