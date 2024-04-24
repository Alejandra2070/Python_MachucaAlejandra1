import json

with open("large-file.json",encoding= "utf-8") as openfile:
    miJSON = json.load(openfile)
'''
print(miJSON)
'''
#print(type(miJSON))
CrearEvento = []
def CrearEventoN(nuevoID, nuevoType, nuevoActor, nuevoRepo):
    crearEvento = {
        "ID":nuevoID,
        "Type":nuevoType,
        "Actor":nuevoActor,
        "Repo":nuevoRepo
    }

CrearEvento.append(CrearEvento)
''' 
for i in range (5):
  print(miJSON[i])
'''
crearEventos=[]
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='CreateEvent'):
        crearEventos.append(miJSON[i])

#print(crearEventos[5]['actor']['id'])
'''
for q in range (5):
    print("#######################")
    print("#### Evento # ",q+1 ,"##")
    print("#######################")
    print("ID: ",crearEventos[q]['id'])
    print("Tipo:",crearEventos[q]['type'])
    print("Actor:")
    print("------- ID:",crearEventos[q]['actor']['id'])

crearEventos[0]['id']=256
with open("eventos.json","w") as outfile:
    json.dump(crearEventos,outfile)
'''

booleano = True
while booleano == True:
 
 print("######################################")
 print("--------------- MENÚ -----------------")
 print("######################################")
 print("1. Crear un evento")
 print("2. Actualizar un evento")
 print("3. Revisar un evento" )
 print("4. Eliminar un evento")
 opcion=input("Ingrese la opción deseada: ")

 if opcion=="1":
    nuevoID = input("Ingresa el ID del evento que quieres agregar: ")
    nuevoType = input("Ingresa el Type del evento que quieres agregar: ")
    nuevoActor = input("Ingresa el Actor del evento que quieres agregar: ")
    nuevoRepo = input("Ingresa el Repo del evento que quieres agregar: ")   
 if opcion=="2":

  break

#Desarrollado por Alejandra Machuca Grupo T2

