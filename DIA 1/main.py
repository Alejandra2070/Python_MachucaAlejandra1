#--------------------------------
#-----DIA 1 CHEAT SHEET PYTHON------
#--------------------------------

#imprimir hola mundo
print("Hola mundooooooooooooooooo!!!")

#Datos primitivos

#Numero
numerito = 1 #nombreVariable = valor
print(numerito)#imprimir(variable)
print(type(numerito))
#imprimir(tipo(variable))

#Decimal
numeritoDecimal = 1.1
print(numeritoDecimal)
print(type(numeritoDecimal))

#Booleano
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito))

#Cadena de texto
texto="MI TIBU"
print(texto)
print(type(texto))

#Ingresa por teclado la informacion
print("¿Cómo se llama?")
nombre = input()
print(f"Me alegro de conocerle, {nombre}")

#Conversion de tipos de variable: tuplas y listas
a_tuple = ('a', 1), 1 ,('f', 2), ('g', 3)
b_list = [1,2,3,4,5]

print(tuple(b_list))
print(list(a_tuple))

#Bucle While

vuelta=1
while vuelta<10:
    print("Vuelta"+str(vuelta))
    vuelta=vuelta+1

#Bucle For

for vuelta in range(1,10):
    print("Vuelta"+str(vuelta))

#Funciones: 

#Solicitar dos números y calcular la suma, resta, multiplicación y división.
print("Ingrese el primer número: ")
n1 = float(input())
print("Ingrese el segundo número: ")
n2 = float(input())
suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
div = n1 / n2
print("La suma es: ",suma)
print("La resta es: ",resta)
print("La multiplicación es: ",mult)
print("La división es: ", div)

#Desarrollado por Alejandra Machuca T.I 1093593725