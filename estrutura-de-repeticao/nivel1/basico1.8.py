idades_validas = 0
idades_invalidas = 0

for i in range(10):
    idade = int(input("Digite a idade: "))

    if idade >= 18:
        idades_validas += 1
    else:
        idades_invalidas += 1

print("Idades válidas:", idades_validas)
print("Idades inválidas:", idades_invalidas)
