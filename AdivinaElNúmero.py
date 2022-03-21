import random
a = random.randint(1, 10)
numero = 0
intentos = 0
limite_intentos=3
sin_intentos = False
print("""ESTE ES EL JUEGO DE ADIVINA UN NUMERO
Elige un número entre el 1 y 10.\n  Tienes 3 intentos.""")
while a != numero and not sin_intentos:
    if intentos < limite_intentos :
       numero =int(input("Esccribe un numero: "))
       intentos+=1
    else:
        sin_intentos = True
if sin_intentos:
    print("Te quedaste sin intentos, has perdido."+"\n" + f"Este era el numero: \n {a}.")    
else:
    print("Has ganado.")
