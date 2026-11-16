nota = 0
for i in range(1, 6):
    valor = float(input("Digite a nota do aluno: "))
    if valor > 10 or valor < 0:
        print("Digite novamente: ")
        valor = float(input("Digite a nota do aluno: "))
    nota += valor
media = nota / 5
print("A média do aluno é:", media)
if media > 6:
    print("Maior que 6")
else:
    if media == 6:
        print("Igual a 6")
    else:
        print("Menor que 6")
