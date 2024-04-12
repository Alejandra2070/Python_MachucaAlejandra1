#------------------------------
#-----------DIA 4--------------
#------------------------------

#imprimir bienvenidos
print("BIENVENIDOSSS!!")
print("En este programa vamos a calcular cuántas monedas se necesitan para un cambio")

def cambio_money(cant):
    monedas = [10, 5, 1]
    number_money = [0, 0, 0]
    for i, moneda in enumerate(monedas):
        number_money[i] = cant // moneda
        cant %= moneda

    return number_money

cant = int(input("Ingresa la cantidad que deseas cambiar: "))
monedas = cambio_money(cant)
print("")
print(f"Para cambiar {cant} se van a necesitar: ")
print("")
print(f"{monedas[2]} monedas de 1")
print(f"{monedas[1]} monedas de 5")
print(f"{monedas[0]} monedas de 10")
print("")
print("Esperamos te haya gustado nuestro programa, te esperamos pronto!!")
print("Que tengas un bonito día")
print("BAYYYYY :D")
