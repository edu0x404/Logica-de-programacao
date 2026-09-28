a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
d = int(input("Digite o valor de d: "))
if a > b and a > c and a > d:
    print(f"O maior número é {a}.")
elif b > a and b > c and b > d:
    print(f"O maior número é {b}.")
elif c > a and c > b and c > d:
    print(f"O maior número é {c}.")
else:
    print(f"O maior número é {d}.")