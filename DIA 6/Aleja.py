#---------------------------
#-----------DIA 6-----------
#---------------------------

cantidad = int(input())
datos = []

for i in range(cantidad):
    dato = input ()
    datos.append(dato)

    if cantidad <=300: #ERROR
     
     datos_ordenados = sorted(datos)
print(datos_ordenados)

lista_sin_duplicados = sorted(list(set(datos)))
print(lista_sin_duplicados)

#Desarrollado por Alejandra Machuca T.I 1093593725

#Primero se ingresa la cantidad de números que va a añadir el usuario