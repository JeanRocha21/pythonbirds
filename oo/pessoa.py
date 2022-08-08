class Pessoa:
    def __init__(self, *filhos, nome=None, idade=29):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self):
        return 'Ola'

if __name__ == '__main__':
    Jean = Pessoa(nome='Jean')
    Pedro = Pessoa(Jean, nome='Pedro')
    print(Pessoa.cumprimentar(Pedro))
    print(Pedro.nome)
    print(Pedro.idade)
    for filho in Pedro.filhos:
        print(filho.nome)


