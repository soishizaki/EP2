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


