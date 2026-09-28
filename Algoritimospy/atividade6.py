import math
numero = int(input("Digite um número: "))
if numero > 0:
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz_quadrada}.")
else:
    print("Por favor, digite um número positivo.")