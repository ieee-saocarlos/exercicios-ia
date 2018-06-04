import random

class Animal:
    def __init__(self, nome, cor, agressividade):
        self.nome = nome
        self.cor = cor
        self.agressividade = agressividade

    def __repr__(self):
        return "Um(a) {} de cor {} com nível de agressividade {}".format(self.nome, self.cor, self.agressividade)

    def conversar(self):
        input("o que você diz para o(a) {} ?".format(self.nome))

        if self.agressividade <= 1:
            print (" o(a) {} foge de voce".format(self.nome))
        elif self.agressividade == 2:
            print (" o(a) {} te encara".format(self.nome))
        else:
            print (" o(a) {} te ataca".format(self.nome))

class Predador(Animal):
    def __init__(self, nome, cor, agressividade, coef_pred):
        super().__init__(nome, cor, agressividade)
        self.coef_pred = coef_pred

    def rolar_dado_da_natureza(self):
        return random.randint(1, 20) * self.coef_pred

    def ataque(self, presa):
        print('O predador ataca a presa')

        ataque = self.rolar_dado_da_natureza()
        fuga = presa.rolar_dado_da_natureza()

        print("ataque:{}".format(ataque))
        print("fuga:{}".format(fuga))

        if ataque>fuga:
            print("O(a) {} comeu o(a) {}".format(self.nome, presa.nome))
            return True

        else:
            print("O(a) {} fugiu do(a) {}".format(presa.nome, self.nome))
            return False

class Presa(Animal):
    def __init__(self, nome, cor, agressividade, coef_fuga):
        super().__init__(nome, cor, agressividade)
        self.coef_fuga = coef_fuga

    def rolar_dado_da_natureza(self):
        return random.randint(1, 20) * self.coef_fuga

def main():

    zebra = Presa('zebra', 'listrada', 2, 8)
    hiena = Predador('hiena', 'malhada', 3, 5)

    hiena.ataque(zebra)


if (__name__ == "__main__"):
    main()






'''Métodos
Namespace
Herança
Polimorfismo
Classe'''