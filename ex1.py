def define_posicoes(linha, coluna, ori, tam):
    pos = []
    
    if ori == "vertical":
        for i in range(tam):
            pos.append([linha + i, coluna])
    else:  
        for i in range(tam):
            pos.append([linha, coluna + i])
    
    return pos 
