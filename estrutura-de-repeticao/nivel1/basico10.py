pares = 0
for i in range(6):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares += 1
print("O número de pares digitados é: ", pares)