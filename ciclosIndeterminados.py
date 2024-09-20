#Juego para determinar un numero aleatorio

import random

aletario = random.randrange(1,20)
numeroIngresado = int(input("Por favor ingresa el numero a adivinar del 1 al 20"))
contadorIntentos = 0

while aletario != numeroIngresado:
    print("Numero ingresado es incorrecto.")
    numeroIngresado = int(input("Por favor ingresa el numero a adivinar del 1 al 20"))
    contadorIntentos += 1

print(f"Muy bien el numero es: {str(numeroIngresado)}, Numero intentos: {str(contadorIntentos)}")