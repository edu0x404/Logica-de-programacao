print("PRATOS")
print("1 - Vegetariano")
print("2 - Peixe")
print("3 - Frango")
print("4 - Carne")

prato = int(input("Escolha o prato: "))

print("\nSOBREMESAS")
print("1 - Abacaxi")
print("2 - Sorvete diet")
print("3 - Mouse diet")
print("4 - Mouse chocolate")

sobremesa = int(input("Escolha a sobremesa: "))

print("\nBEBIDAS")
print("1 - Chá")
print("2 - Suco de laranja")
print("3 - Suco de melão")
print("4 - Refrigerante diet")

bebida = int(input("Escolha a bebida: "))

if prato == 1:
    cal_prato = 180
elif prato == 2:
    cal_prato = 230
elif prato == 3:
    cal_prato = 250
else:
    cal_prato = 350

if sobremesa == 1:
    cal_sobremesa = 75
elif sobremesa == 2:
    cal_sobremesa = 110
elif sobremesa == 3:
    cal_sobremesa = 170
else:
    cal_sobremesa = 200

if bebida == 1:
    cal_bebida = 20
elif bebida == 2:
    cal_bebida = 70
elif bebida == 3:
    cal_bebida = 100
else:
    cal_bebida = 65

total = cal_prato + cal_sobremesa + cal_bebida

print("Total de calorias:", total, "cal")