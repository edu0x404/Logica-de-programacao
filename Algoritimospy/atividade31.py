A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if A + B > C and A + C > B and B + C > A:
    if A > B:
        A, B = B, A
    if B > C:
        B, C = C, B
    if A > B:
        A, B = B, A

    if A ** 2 + B ** 2 == C ** 2:
        print("Triângulo Retângulo")
    elif A ** 2 + B ** 2 > C ** 2:
        print("Triângulo Acutângulo")
    else:
        print("Triângulo Obtusângulo")
else:
    print("Os valores não podem formar um triângulo.")