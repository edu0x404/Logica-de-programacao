rodada = 0
soma = 0
media = 0
maior = 0
rodadas = 0
for i in range(1, 7):
    p1 = int(input("Digite a pontuação da " + str(rodada + 1) + "ª rodada: ")) 
    rodada += 1
    soma += p1
    if p1 > maior:
        maior = p1
        rodadas = rodada
print("Pontuação total do jogador: ", soma)
media = soma / 6
print("Média de pontos por rodada: ", media)
print("O maior foi "+str(maior)+" na rodada "+str(rodadas))

