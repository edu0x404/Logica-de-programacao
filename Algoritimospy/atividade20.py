a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if a <= b:
    menor, maior = a, b
else:
    menor, maior = b, a

print(f"Quadrado do menor ({menor}): {menor ** 2}")

if maior >= 0:
    print(f"Raiz quadrada do maior ({maior}): {maior ** 0.5}")
else:
    print(f"Não é possível calcular a raiz quadrada de {maior} (número negativo).")   