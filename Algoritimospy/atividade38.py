freq = float(input("Digite a frequência (%): "))
nota = float(input("Digite a nota: "))

if freq <= 75:
    print("REPROVADO")
elif nota <= 3:
    print("REPROVADO")
elif nota <= 7:
    print("EXAME")
else:
    print("APROVADO")