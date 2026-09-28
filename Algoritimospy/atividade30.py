A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if A + B > C and A + C > B and B + C > A:
    if A == B and B == C:
        print("Triângulo equilátero")
    elif A == B or A == C or B == C:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Os valores não podem formar um triângulo.")