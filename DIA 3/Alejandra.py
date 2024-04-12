#-------------------------
#-------DIA 3-------------
#-------------------------

#Números primos
def función1():
   print("Esta es la primera función de los ejercicios")
def num_primos(n):
     
     if n <= 1:
       return False
     elif n <= 3:
       return True
     elif n % 2 == 0 or n % 3 == 0:
       return False
     i = 5
     while i * i <= n:
       if n % i == 0 or n % (i + 2) == 0:
        return False
     i += 6
     return True
def menu_opciones():
      print("\nBIENVENIDOS!!!!")
      print("Vamos a verificar cuáles son los números primos")
      print("Seleccione una de las opciones de nuestro menú: ")
      print("1: Verificar si el número que ingreses es primo")
      print("2: Salir de el programa")
      print("3: Ver información adicional sobre los números primos")
      print("")
def informaciónAdic():
      print("\nUn número primo, es aquel número entero mayor que 1, que tan solo tienen dos (2) divisores. Estos divisores son el número 1 y el mismo número y, el resultado de la división, siempre es un número entero.")
      print("")
def main():
   while True:
      menu_opciones()
      opc = input("Ingresa una de las opciones de nuestro menú: ")
      print("")
      if opc == "1":
         n = int(input("Ingrese el número que deseas verificar: "))
         if num_primos(n):
            print(f"{n} es un número primo")
         else:
            print(f"{n} no es un número primo")
      elif opc =="2":
         print("Este es el fin de nuestro programa. Esperamos que regreses muy pronto :D")
         break
      elif opc =="3":
         informaciónAdic()
      else:
         print("Esta opción no pertenece a nuestro menú de opciones, ingresa otra")
if __name__ == "__main__":
   main()


#Contraseña segura
def funcion2():
    print("Esta es la segunda función de los ejercicios")

import random
import string
    
def generarcontraseña(longitud, mayus, minus,nums, simbs):
    caracteres = ""
    if mayus:
        caracteres += string.ascii_uppercase
    if minus:
        caracteres += string.ascii_lowercase
    if nums:
        caracteres += string.digits
    if simbs:
        caracteres += string.punctuation
    contraseña="".join(random.choice(caracteres)for _ in range(longitud))
    range(longitud)
    return contraseña
def main():
    print("BIENVENIDOS!!!!")
    print("Este programa crea contraseñas seguras en base a tus preferencias")
    while True:
        try:
            longitud=int(input("Ingrese la longitud para generar su contraseña: "))
            break
        except ValueError:
            print("Ingrese un número entero: ")
    mayus=input("Quiere que su contraseña contenga mayúsculas? (s/n) ").lower()=='s'
    minus=input("Quiere que su contraseña contenga minúsculas? (s/n) ").lower()=='s'
    nums=input("Quiere que su contraseña contenga números? (s/n) ").lower()=='s'
    simbs=input("Quiere que su contraseña contenga símbolos? (s/n) ").lower()=='s'
    contraseñanueva=generarcontraseña(longitud, mayus, minus, nums, simbs)
    print("Esta es su nueva contraseña: ",contraseñanueva)
    while True:
        generarotra=input("Te gustaría crear una nueva contraseña? (s/n)").lower()
        if generarotra=='s':
            main()
        elif generarotra=='n':
            print("Te agradecemos por usar nuestro programa. Esperamos vuelvas pronto!! :D")
            break
        else:
            print("Si te gustaría crear otra contraseña ingresa 's' o 'n' para salir")
if __name__ == "__main__":
    main()





    
