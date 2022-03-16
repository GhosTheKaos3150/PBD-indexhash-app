from classes.tuplas import Tupla

class Pagina:
    num_pagina: int
    tuplas: list
    lim: int

    def __init__(self, num_pagina, lim):
        self.num_pagina = num_pagina
        self.lim = lim
        self.tuplas = []
    
    def is_full(self):
        if len(self.tuplas) == self.lim:
            return True
        return False

    def create_tupla(self, value):
        self.tuplas.append(Tupla(value, self.num_pagina))
    
    def read_tuple_by_pk(self, pk):
        for tupla in self.tuplas:
            if tupla.pk == pk:
                return tupla

    def update_tuple_by_pk(self, pk, new_value):
        for index, tupla in enumerate(self.tuplas):
            if tupla.pk == pk:
                self.tuplas[index].pk = new_value
                self.tuplas[index].value = new_value

    def delete_tupla_by_pk(self, pk):
        for index, tupla in enumerate(self.tuplas):
            if tupla.pk == pk:
                self.tuplas.pop(index)
    
    def to_string(self):
        str_final = ""
        for index, tupla in enumerate(self.tuplas):
            str_final += f"{index}. {tupla.valor}"
            if index != len(self.tuplas)-1:
                str_final += "\n"
        
        return str_final
