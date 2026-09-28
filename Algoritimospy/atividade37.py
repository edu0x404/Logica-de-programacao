idade = int(input("Digite a idade: "))
peso = float(input("Digite o peso em kg: "))

if idade >= 12:
    if peso >= 60:
        dosagem = 1000
    else:
        dosagem = 875
else:
    if peso >= 5 and peso <= 9:
        dosagem = 125
    elif peso >= 9.1 and peso <= 16:
        dosagem = 250
    elif peso >= 16.1 and peso <= 24:
        dosagem = 375
    elif peso >= 24.1 and peso <= 30:
        dosagem = 500
    elif peso > 30:
        dosagem = 750
    else:
        dosagem = 0

if dosagem > 0:
    ml = dosagem / 500
    gotas = ml * 20

    print("Dosagem:", dosagem, "mg")
    print("Volume:", ml, "ml")
    print("Tomar", gotas, "gotas por dose.")
else:
    print("Peso fora da faixa especificada.")