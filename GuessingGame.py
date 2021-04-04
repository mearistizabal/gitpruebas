from typing import Any, Union

print("Bienvenido al juego de Adivina el número")
import random
numInferior = 1
numSuperior = 100
number_to_guess = random.randint(numInferior, numSuperior)
guess = int(input("Adivina el número, entre {} y {}:".format(numInferior, numSuperior)))
numero_intentos = 1
numIngresados = []
numIngresados.append(guess)
while number_to_guess !=guess:
    print("Número equivocado. Sigue intentando")
    if numero_intentos ==4:
        break
    elif guess < number_to_guess:
        print("El número que buscamos es mayor")
    else:
        print("El número que buscamos  es menor")
    print("Llevas {} intentos:".format(numero_intentos))
    guess=int(input("Ingresa otro número:"))
    numero_intentos +=1
    numIngresados.append(guess)

if number_to_guess == guess:
    print("Bien hecho. Adivinaste!")
    print("Tomaste" , numero_intentos , "intentos para adivinar")
else:
    print("Lo siento, perdiste")
    print("El número que debías adivinar era ",number_to_guess)
print("Los números que ingresaste fueron: ",numIngresados)
print("Juego terminado")
