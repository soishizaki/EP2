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

print(frota)