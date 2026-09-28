saldo = float(input("Digite o saldo médio: "))
if saldo <= 500:
    credito = 0
elif saldo <= 1000:
    credito = saldo * 0.30
elif saldo <= 3000:
    credito = saldo * 0.40
else:
    credito = saldo * 0.50
print(f"Saldo médio: R$ {saldo:.2f}")
print(f"Valor do crédito: R$ {credito:.2f}")   