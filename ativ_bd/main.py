from flask import Flask
from flask_cors import CORS
from routes.hash_route import hash_route
from routes.index import index_route
# from classes.bucket import Bucket
# from classes.pagina import Pagina
# from classes.indice_hash import IndiceHash

if __name__ == "__main__":
    # cardinalidade = 0
    # tamanho_pagina = 16
    # n_paginas = 32

    # paginas = []

    # with open("./words.txt", "r") as file:
    #     lines = file.readlines()

    # for line in lines:
    #     line = line.split(" ")
    #     for word in line:
    #         word = word.rsplit("\n")
    #         if not len(paginas) or paginas[-1].is_full():
    #             paginas.append(Pagina(len(paginas), tamanho_pagina))
        
    #         paginas[-1].create_tupla(word if type(word) is str else word[0])
    #         cardinalidade += 1

    # # for pagina in paginas:
    # #     print("=========\n"+str(pagina.num_pagina)+"\n=========\n")
    # #     print(pagina.to_string())

    # indice = IndiceHash(128, 8, cardinalidade)

    # for pagina in paginas:
    #     for tupla in pagina.tuplas:
    #         indice.definir_indice(tupla)

    # indice.print_indice()
    # print("----------")
    # print(indice.procura_inhash("a", as_str=True))
    # print("----------")

    app = Flask(__name__)
    CORS(app)
    
    app.register_blueprint(hash_route)
    app.register_blueprint(index_route)

    app.run(host="localhost", port="3150")
