from classes.pagina import Pagina
from classes.indice_hash import IndiceHash
from util.bcolors import Bcolors as bcolors

def create_paginas(text, tamanho_pagina):
    if type(text) is str:
        text = text.split(" ")

    print(f'{bcolors.WARNING}Criando Paginas Baseado no Texto...{bcolors.ENDC}')
    

    paginas = []
    cardinalidade = 0
    for word in text:
        word = word.rsplit("\n")
        if not len(paginas) or paginas[-1].is_full():
            paginas.append(Pagina(len(paginas), tamanho_pagina))
        
        paginas[-1].create_tupla(word if type(word) is str else word[0])
        cardinalidade += 1

    return paginas, cardinalidade

def create_indice(paginas, size, cardinalidade, overflow=8):
    print(f'{bcolors.WARNING}Criando Indices...{bcolors.ENDC}')

    indice = IndiceHash(size, overflow, cardinalidade)

    for pagina in paginas:
        for tupla in pagina.tuplas:
            indice.definir_indice(tupla)
    
    return indice
