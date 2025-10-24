# Item 7
from funcoes import *

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

embarcacoes = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4)
]

for tipo, comprimento, repeticoes in embarcacoes:
    contador = 0
    while contador < repeticoes:
        print(f"Insira as informações referentes ao navio {tipo} que possui tamanho {comprimento}")

        linha = int(input("Linha: "))
        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Linha: "))

        coluna = int(input("Coluna: "))
        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Coluna: "))

        if comprimento == 1:
            orientacao = "vertical"
        else:
            op = int(input("[1] Vertical [2] Horizontal >"))
            if op == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"

        if posicao_valida(frota, linha, coluna, orientacao, comprimento):
            preenche_frota(frota, tipo, linha, coluna, orientacao, comprimento)
            contador += 1
        else:
            print("Esta posição não está válida!")


# Item 8
frota_oponente = {
    'porta-aviões': [[[9, 1], [9, 2], [9, 3], [9, 4]]],
    'navio-tanque': [[[6, 0], [6, 1], [6, 2]], [[4, 3], [5, 3], [6, 3]]],
    'contratorpedeiro': [[[1, 6], [1, 7]], [[0, 5], [1, 5]], [[3, 6], [3, 7]]],
    'submarino': [[[2, 7]], [[0, 6]], [[9, 7]], [[7, 6]]]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogadas_anteriores = []
jogadas_oponente = []
imprime = True

while True:
    if imprime:
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    imprime = True

    linha = int(input("Jogador, qual linha deseja atacar? "))
    while linha < 0 or linha > 9:
        print("Linha inválida!")
        linha = int(input("Jogador, qual linha deseja atacar? "))

    coluna = int(input("Jogador, qual coluna deseja atacar? "))
    while coluna < 0 or coluna > 9:
        print("Coluna inválida!")
        coluna = int(input("Jogador, qual coluna deseja atacar? "))

    if [linha, coluna] in jogadas_anteriores:
        print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        imprime = False
        continue

    jogadas_anteriores.append([linha, coluna])
    faz_jogada(tabuleiro_oponente, linha, coluna)
    
    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        break