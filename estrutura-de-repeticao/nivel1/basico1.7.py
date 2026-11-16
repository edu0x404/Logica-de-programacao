positivos = 0
zeros = 0
negativos = 0
for i in range(6):
    numero = int(input("Digite um número: "))
    if numero > 0:
        positivos += 1
    elif numero == 0:
        zeros += 1
    else:
        negativos += 1
print("Positivos:", positivos)
print("Zeros:", zeros)
print("Negativos:", negativos)