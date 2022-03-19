from flask import Flask, make_response, Blueprint, abort, request
from util.bcolors import Bcolors as bcolors
import util.hash_functions as uhf
import armazenamento as storage

hash_route = Blueprint("hash_route", __name__)


@hash_route.route("/hash/initqm")
def get_storage_init():
    return make_response({"status": "OK", "init": bool(storage.paginas)}, 200)


@hash_route.route("/hash/search/<word>", methods=["GET"])
def get_word_on_hash(word):
    print(f'{bcolors.WARNING}Procurando palavra "{word}" no hash...{bcolors.ENDC}')

    try:
        res = storage.indice.procura_inhash(word)
        print(res)
    except Exception as e:
        print(e)
        print(f'{bcolors.FAIL}Palavra não encontrada. Retornando...{bcolors.ENDC}')
        return make_response({"status": "NOT FOUND"}, 404)
    
    if res == "Não encontrado":
        print(f'{bcolors.FAIL}Palavra não encontrada. Retornando...{bcolors.ENDC}')
        return make_response({"status": "NOT FOUND"}, 404)

    print(f'{bcolors.OKGREEN}Palavra Encontrada! Retornando...{bcolors.ENDC}')
    return make_response({"status": "OK", "data": res}, 200)


@hash_route.route("/hash", methods=["POST", "DELETE"])
def post_message_to_hash():
    # EXPECTED for POST
    # { 
    #   "text": str, 
    #   "tamanho_pag": int,
    #   "tamanho_bucket": int
    # }

    if request.method == "DELETE":
        print(f'{bcolors.WARNING}Deletando BD com Indice Hash...{bcolors.ENDC}')

        storage.reset()

        print(f'{bcolors.OKGREEN}BD Deletado com Sucesso! Retornando...{bcolors.ENDC}')
        return make_response({"status": "OK"}, 200)

    else:
        print(f'{bcolors.WARNING}Criando BD com Indice Hash...{bcolors.ENDC}')

        info = request.json
        msg = info["text"]

        if not type(msg) is str:
            print(f'{bcolors.FAIL}Texto da Mensagem não é STRING. Retornando...{bcolors.ENDC}')
            return make_response({"status": "BAD REQUEST"}, 400)

        try:
            storage.paginas, cardn = uhf.create_paginas(msg, info["t_pag"])
            storage.indice = uhf.create_indice(storage.paginas, info["t_bucket"], cardn)
        except Exception as e:
            print(e)
            print(f'{bcolors.FAIL}Não foi possível criar BD. Retornando...{bcolors.ENDC}')
            return make_response({"status": "INTERNAL SERVER ERROR"}, 500)

        print(f'{bcolors.OKGREEN}BD Criado com Sucesso! Retornando...{bcolors.ENDC}')
        return make_response({"status": "OK"}, 200)
