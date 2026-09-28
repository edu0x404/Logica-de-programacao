valor_de_compras = float(input("Digite o valor das compras: "))
if valor_de_compras < 10:
    lucro = valor_de_compras * 0.7
if valor_de_compras >= 10 and valor_de_compras <= 30:
    lucro = valor_de_compras * 0.5
if valor_de_compras > 30:
    lucro = valor_de_compras * 0.4
if valor_de_compras >= 50:
    lucro = valor_de_compras * 0.3
print(f"O lucro do comerciante é: R${lucro:.2f}")