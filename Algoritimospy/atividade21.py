peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
if imc < 20:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Acima do peso")
elif imc < 40:
    print("Obeso")
else: 
    print("Obesidade mórbida")