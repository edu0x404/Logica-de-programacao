n = int(input("Digite um número: "))
soma = 0
for i in range(1, n+1):
    n2 = int(input("Digite outro número: "))
    soma += n2
    media = soma / n
print("A soma dos números é: ", soma)
print("A média dos números é: ", media)
