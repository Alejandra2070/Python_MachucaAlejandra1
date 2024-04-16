#-----------------------------------
#-------------DIA 6-----------------
#-----------------------------------

def sumas(nums, target):
    dicci_nums = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in dicci_nums:
            return [dicci_nums[complement], i]
        dicci_nums[num] = i
    return f"No se encontraron dos números que sumen {target}"

nums_ingresados = input()
nums_strings = nums_ingresados.split()
nums = [int(num_str) for num_str in nums_strings]

target = int(input())

result = sumas(nums, target)
print(f"{result}")

#Debemos ingresar los numeros separados por espacios
#Luego damos enter e ingresamos el target
#Por último nos darán los índices

#Desarrollado por Alejandra Machuca T.I 1093593725