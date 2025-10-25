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

            for pos in posicoes_navio:
                linha = pos[0]
                coluna = pos[1]

                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break

            if afundado:
                navios_afundados += 1

    return navios_afundados

# Item 6 
def posicao_valida(frota, linha, coluna, ori, tam):
    posicoes_novas = define_posicoes(linha, coluna, ori, tam)
    
    for pos in posicoes_novas:
        linha_pos = pos[0]
        coluna_pos = pos[1]
        if linha_pos < 0 or linha_pos >= 10 or coluna_pos < 0 or coluna_pos >= 10:
            return False

    for nome_navio in frota:
        lista_navios = frota[nome_navio]
        for posicoes_navio in lista_navios:
            for posicao_existente in posicoes_navio:
                linha_existente = posicao_existente[0]
                coluna_existente = posicao_existente[1]
                if [linha_existente, coluna_existente] in posicoes_novas:
                    return False
    
    return True

# Item 8
def monta_tabuleiros(tab_j, tab_op):
    texto_final = ''
    texto_final += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto_final += '_______________________________      _______________________________\n'
    for idx in range(10):
        jg = '  '.join(str(c) for c in tab_j[idx])
        op = '  '.join(str(c) if str(c) in ['X', '-'] else '0' for c in tab_op[idx])
        texto_final += f'{idx}| {jg}|     {idx}| {op}|\n'
    return texto_final

