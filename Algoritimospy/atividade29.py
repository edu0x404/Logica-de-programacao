A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if A + B > C and A + C > B and B + C > A:
    print("Os valores podem formar um triângulo.")
else:
    print("Os valores não podem formar um triângulo.")