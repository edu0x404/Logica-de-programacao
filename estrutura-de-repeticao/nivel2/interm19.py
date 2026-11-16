menores = 0
adultos = 0
idosos = 0
for i in range(1, 7):
    idade = int(input("Digite a idade: "))
    if idade < 12:
        menores += 1
    elif idade >= 12 and idade <= 59:
        adultos += 1
    else:
        idosos += 1
print("Menores de 12 anos:", menores)
print("Entre 12 e 59 anos:", adultos)
print("60 anos ou mais:", idosos)