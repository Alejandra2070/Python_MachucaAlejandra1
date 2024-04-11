#----------------------------
#----------DIA 2-------------
#----------------------------

#imprimir bienvenidos
print("BIENVENIDOSSS!!!!:D")

#Secuencia de Fibonacci

pos = int(input("Escriba que posición quiere de la serie Fibonacci: "))
ans = input("Desea ver el resultado de toda la serie? (S/N): ")
iniFibo = 0
finFibo = 1
for x in range(0,pos):
    if x ==0:
        finFibo=0
    elif x ==1:
        finFibo=1
    if ans =="S" or ans=="s":
        print(f'Posición:{x+1:>4}--Valor en la serie de Fibonacci: {finFibo:>10}')
    sum = finFibo
    finFibo = finFibo + iniFibo
    iniFibo = finFibo - iniFibo
print(f"\nPosición Final:{x+1:>4}--Valor en la serie de Fibonacci:{sum:>10}")
#Desarrollado por Alejandra Machuca T.I 1093593725
    

