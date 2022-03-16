class Bucket:

    hash: int
    lim: int
    valor: list
    overflow: bool

    def __init__(self, hash, lim):
        self.hash = hash
        self.lim = lim
        self.valor = []
        self.overflow = False

    def add_value(self, valor):
        if self.is_full() and not self.have_overflow():
            self.set_overflow(Bucket(self.hash, self.lim))
            self.valor[-1].add_value(valor)
        elif self.have_overflow():
            self.valor[-1].add_value(valor)
        else:
            self.valor.append(valor)

    def have_overflow(self):
        return self.overflow

    def many_overflows(self):
        return (1 if self.overflow else 0) + self.valor[-1].many_overflows() if self.overflow else 0

    def set_overflow(self, overflow):
        self.valor[-1] = overflow
        self.overflow = True

    def is_full(self):
        if len(self.valor)-1 == self.lim:
            return True
        return False
