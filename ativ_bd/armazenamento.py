from classes.indice_hash import IndiceHash
from classes.pagina import Pagina

paginas: Pagina = None
indice: IndiceHash = None

def reset():
    global paginas, indice

    paginas = None
    indice = None
