#--------------------------
#---------DIA 2------------
#--------------------------

#Intentos

import random

randomNum = random.randint (1, 100)
intents = 0

print("Intenta adivinar el número con 10 intentos")

while intents < 10:
   print(f"Intentos {intents}")

   intent = int(input())
   intents += 1

   if intent < randomNum:
     print("El número es muy bajo")

   elif intent > randomNum:
     print("El número es muy alto")

   else: 
     break
    
if intent == randomNum:
    print(f"¡¡¡FELICIDADES!!! Adivinaste el número correcto! Este es: {randomNum}")
    print(f"Adivinaste el número correcto en el intento: {intents-1}")
else: 
    print(f"Ya no tienes más intentos, el número correcto era: {randomNum}")

#Desarrollado por Alejandra Machuca T.I 1093593725