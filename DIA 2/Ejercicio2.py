#--------------------
#------DIA 2---------
#--------------------

#Juego Interactivo

import random

print("Bienvenido al juego 'Adivina el número secreto'!")
print("Después de cada intento, recibirás una pista para ayudarte")
print("Sin más que decir, ¡empecemos!")

num_secret = random.randint(1, 100)

intentos = 0
adivin = False

while not adivin:
    suposición = input("Ingresa tu suposición (entre 1 y 100):")

    if not suposición.isdigit():
        print("Ingresa un número válido")
        continue

    suposición = int(suposición)

    if suposición < 1 or suposición > 100:
       print("El número debe estar en el rango de 1 a 100")
       continue
    intentos += 1

    if suposición < num_secret:
       print("Demasiado bajo. ¡Inténtalo de nuevo!")
    elif suposición > num_secret:
       print("Demasiado alto. ¡Inténtalo de nuevo!")
    else:
       print(f"¡MUCHAS FELICIDADES! ¡Adivinaste el número en {intentos} intentos!")
       adivin = True

jugar_nuev = input("Deseas jugar nuevamente? (si/no): ")

if jugar_nuev.lower() == 'si':
    num_secret = random.randint(1, 100)
    intentos = 0
    adivin = False
    print("¡Muy bien! ¡Jugaremos nuevamente!")
else: 
    print("Gracias por jugar. ¡Vuelve pronto! :D ")    

#Desarrollado por Alejandra Machuca T.I 1093593725