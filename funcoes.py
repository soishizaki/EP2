# Item 1
def define_posicoes(linha, coluna, ori, tam):
    pos = []
    
    if ori == "vertical":
        for i in range(tam):
            pos.append([linha + i, coluna])
    else:  
        for i in range(tam):
            pos.append([linha, coluna + i])
    
    return pos 

# Item 2
def preenche_frota(frota, nome_navio, linha, coluna, ori, tam):
    pos = define_posicoes(linha, coluna, ori, tam)

    if nome_navio not in frota:
        frota[nome_navio] = [pos]
    else:
        frota[nome_navio].append(pos)
    
    return frota

# Item 3 

def faz_jogada(tabuleiro, linha, coluna):
    valor = tabuleiro[linha][coluna]
    if valor not in (0, 1):
        return tabuleiro  # ignora se já foi jogado antes
    
    if valor == 1: 
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    
    return tabuleiro

# Item 4 
def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)
    
    for nome_navio in frota:
        navios = frota[nome_navio]
        for posicoes_navio in navios:
            for pos in posicoes_navio:
                linha = pos[0]
                coluna = pos[1]
                tabuleiro[linha][coluna] = 1
    
    return tabuleiro

# Item 5 
def afundados(frota, tabuleiro):
    navios_afundados = 0  

    for nome_navio in frota:
        lista_navios = frota[nome_navio]

        for posicoes_navio in lista_navios:
            afundado = True 

            for posicao in posicoes_navio:
                linha = posicao[0]
                coluna = posicao[1]

                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break

            if afundado:
                navios_afundados += 1

    return navios_afundados

