produtos = int(input("Digite a quantidade de produtos: "))
preço_total = 0
for i in range(1, produtos + 1):
    pro = int(input("Digite o preço do produto: "))
    preço_total += pro
    if pro == 0:
        print("Compra vazia")
        break
print("Preço total da compra: ", preço_total)
print("Quantidade de produtos comprados: ", produtos)