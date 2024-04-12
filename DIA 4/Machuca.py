#-------------------------------
#------------DIA 4--------------
#-------------------------------

#imprimir bienvenidos
print("BIENVENIDOSSS!!! :D")
print("En este programa vamos a calcular el mínimo de monedas  necesarias para cambiar el valor dado")
import string

dinero = int(input("Ingrese la cantidad que desea cambiar: "))

lista = [1, 5, 10]

for i in lista:
 
    if dinero <= i:
     queda=dinero//i
    print("Existen " + string(queda) + ("billetes" if dinero <=1 else "monedas") + " de " + string (i) + "pesos" )
    dinero = dinero % i

    if dinero <= i:
     queda=dinero//i
    print("Existen " + string(queda) +  "billetes de 5")
    dinero = dinero % i

    if dinero <= i:
     queda=dinero//i
    print("Existen " + string(queda) +  "billetes de 10")
    dinero = dinero % i
    