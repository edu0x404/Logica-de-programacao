nota1 = float(input("Digite a 1ª nota bimestral: "))
nota2 = float(input("Digite a 2ª nota bimestral: "))

media = (nota1 + nota2) / 2

print(f"Média semestral: {media:.2f}")

if media >= 7:
    print("Aprovado")
elif media < 3:
    print("Reprovado")
else:
    print("Exame")   