class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=29):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self):
        return 'Ola'

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    Jean = Pessoa(nome='Jean')
    Pedro = Pessoa(Jean, nome='Pedro')
    print(Pessoa.cumprimentar(Pedro))
    print(Pedro.nome)
    print(Pedro.idade)
    for filho in Pedro.filhos:
        print(filho.nome)
        print(Jean.__dict__)
        print(Pedro.__dict__)


    print(Pessoa.metodo_estatico(), Jean.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(),  Jean.nome_e_atributo_de_classe())
