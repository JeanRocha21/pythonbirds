'''

    Exemplo:
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1

# >>> testando direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    3
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    1
    >>> carro.calcular_direcao()
    'Oeste'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Sul'

'''

class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao
    def calcular_velocidade(self):
        return self.motor.velocidade
    def acelerar(self):
        return self.motor.acelerar()
    def frear(self):
        return self.motor.frear()
    def calcular_direcao(self):
        return self.direcao.valor
    def girar_a_direita(self):
        return self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()
    

class Motor:
    def __init__(self):
        self.velocidade = 0
    def acelerar(self):
        self.velocidade += 1
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

NORTE = 'Norte'
SUL ='Sul'
LESTE ='Leste'
OESTE = 'Oeste'

class Direcao:
    rotacao_a_direita = {NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE}
    rotacao_a_esquerda = {NORTE:OESTE, LESTE:NORTE, SUL:LESTE, OESTE:SUL}

    def __init__(self):
        self.valor = NORTE
    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita[self.valor]

    def girar_a_esquerda(self):
         self.valor = self.rotacao_a_esquerda[self.valor]
        
