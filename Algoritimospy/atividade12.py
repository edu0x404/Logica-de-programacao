salario_bruto = float(input("Digite o salário bruto: "))
prestacao = float(input("Digite o valor da prestação: "))
limite = salario_bruto * 0.3
if prestacao <= limite:
    print("Empréstimo pode ser concedido.") 
else:
    print("Empréstimo não pode ser concedido.")
