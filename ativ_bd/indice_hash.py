from math import floor, ceil
from bucket import Bucket
from tuplas import Tupla


class IndiceHash:

    vetor_hash: list
    size_vetor: int
    max_overflow: int
    collisions: int

    def __init__(self, size, overflow, card):
        self.size_vetor = size
        self.max_overflow = overflow
        self.collisions = 0

        self.vetor_hash = []
        for i in range(ceil((card/size)+overflow)):
            self.vetor_hash.append(Bucket(i, size))

    def definir_indice(self, info: Tupla, rec=0):
        if self.vetor_hash[self.calculo_hash(info.pk)+rec].is_full() and \
                not self.vetor_hash[self.calculo_hash(info.pk)+rec].have_overflow:
            self.vetor_hash[self.calculo_hash(info.pk) + rec].set_overflow(
                Bucket(
                    self.vetor_hash[self.calculo_hash(info.pk)+rec].hash,
                    self.vetor_hash[self.calculo_hash(info.pk)+rec].lim
                )
            )
            self.vetor_hash[self.calculo_hash(info.pk) + rec].add_value(info)
            self.collisions += 1
        elif self.vetor_hash[self.calculo_hash(info.pk)+rec].is_full() and \
                self.vetor_hash[self.calculo_hash(info.pk)+rec].have_overflow:
            self.vetor_hash[self.calculo_hash(info.pk) + rec].add_value(info)
            self.collisions += 1
        else:
            self.vetor_hash[self.calculo_hash(info.pk) + rec].valor.append(info)

    def calculo_hash(self, indice: str):
        indice = [ord(x) for x in indice]
        word_hash = ""
        for i in indice:
            word_hash += str(i)
        

        size = len(str(len(self.vetor_hash)))
       
        if len(word_hash) > 0:
            word_hash = int(word_hash[-1])
            
        else:
            word_hash = int(word_hash[-size:-1])
        
        word_hash = int(word_hash)

        s_hash = floor(word_hash)
        #print("s_hash = ",word_hash)
        # s_hash = floor(word_hash/(10^len(self.vetor_hash)))
        #EX: WORD HASH = 12345678 / LEN.VETOR HASH = 4
        #S_HASH = FLOOR(12345678 / 10^4)
        #S_HASH = FLOOR(1234.5678)
        #S_HASH = 1234
        return s_hash

    def procura_inhash(self, valor, bucket=None, as_str=False):
        if bucket is None:
            hash_c = self.calculo_hash(valor)

            if len(self.vetor_hash) > hash_c:
                for tupla in self.vetor_hash[hash_c].valor:
                    if tupla.valor == valor:
                        return f"Pagina: {tupla.page}" if as_str else tupla.page
                else:
                    return self.procura_inhash(valor, self.vetor_hash[hash_c].valor[-1], as_str)
        else:
            for tupla in bucket.valor:
                if tupla.valor == valor:
                    return f"Pagina: {tupla.page} [COM COLISÃO]" if as_str else tupla.page
            else:
                if bucket.is_full():
                    return self.procura_inhash(valor, bucket.valor[-1], as_str)

            return "Não encontrado"

        return "Não encontrado"

    def print_indice(self):
        for bucket in self.vetor_hash:
            print(f"==>bucket {bucket.hash+1}")
            if len(bucket.valor):
                for i, value in enumerate(bucket.valor):
                    if not type(value) is Bucket:
                        print(f"{i+1}. '{value.valor}', {value.page}")
                    else:
                        print(f"{i+1}. OVERFLOW")
            else:
                print("Bucket Vazio")

        self.print_overflow()
        self.print_collisions()

    def print_collisions(self):
        print("Collisions:", self.collisions)

    def print_overflow(self):
        overflows = 0
        for bucket in self.vetor_hash:
            if bucket.have_overflow():
                overflows += bucket.many_overflows()

        print("\nOverflow:", overflows)
