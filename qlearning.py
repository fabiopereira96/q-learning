import util_estados
import numpy as npy
import pprint   
import random

class Qlearning:
    
    _qMap  = []
    _piMap = []
    i      = -1
    j      = -1
    alpha  = -1
    gamma  = -1
    n      = 0
    
    def __init__(self, mapa, i, j, x, y, n):
        self._oMap = mapa
        self.i = i
        self.j = j
        self._qMap = []
        self._piMap = []
        self.alpha = x
        self.gamma = y
        self.n = n
    
    def getQMap(self):
        return self._qMap

    def getOMap(self):
        return self._oMap
    
    def getPiMap(self):
        return self._piMap    
    
    def getAdMap(self):
        return [self.alpha, self.gamma]
        
    def getNMap(self):
        return self.n

    def setPiMap(self, piMap):
        self._piMap = piMap
    
    def fiilPiMap(self):
        self.setPiMap(self._oMap)
        for li in range(0, int(self.i)):
            for col in range(0, int(self.j)):
                estado = self._oMap[li][col]
                if estado == '-':
                    acao = npy.argmax(self._qMap[li, col])
                    self._piMap[li][col] = util_estados.mapea_acao(acao, "simbolo")

    def calculateInitialQMap(self):
        d = 4
        self._qMap = npy.array([[[0 for k in range(d)]
                       for j in range(self.j)] for i in range(self.i)]).astype("float32")
        for li in range(0, int(self.i)):
            for col in range(0, int(self.j)):
                cost = npy.array([0, 0, 0, 0]).astype("float32")
                self._qMap[li][col] = cost
    
    def updateQMap(self, estado_atual, proximo_estado, acao):
        rsa = float(util_estados.cost_by_content(self._oMap[estado_atual[0]][estado_atual[1]]))
        qsa = float(self._qMap[estado_atual[0]][estado_atual[1]][acao])
        novo_q = qsa + float(self.alpha) * \
            (rsa + float(self.gamma) *
             float(npy.amax(self._qMap[proximo_estado[0]][proximo_estado[1]])) - qsa)
        self._qMap[estado_atual[0]][estado_atual[1]][acao] = novo_q

        # normalizacao 0-1
        rn = self._qMap[estado_atual[0]][estado_atual[1]][self._qMap[estado_atual[0]][estado_atual[1]] > 0] / npy.sum(self._qMap[estado_atual[0]][estado_atual[1]][self._qMap[estado_atual[0]][estado_atual[1]] > 0])
        self._qMap[estado_atual[0]][estado_atual[1]][self._qMap[estado_atual[0]][estado_atual[1]] > 0] = rn
        
        return util_estados.cost_by_content(self._oMap[estado_atual[0]][estado_atual[1]])

    def executeQLearning(self):
        n_episodes = 20  # Fixado para teste
        estado_atual = []
        proximo_estado = []
        # random_state = npy.random.RandomState(100, 100)
        for e in range(int(n_episodes)):

            # estado_atual = util_estados.cria_estado_aleatorio(self.i, self.j)
            estado_atual = [3, 3]
            goal = False
            for i in range(0, int(self.n)):

                caminhos = util_estados.ramifica_estado(
                    self._oMap, estado_atual[0], estado_atual[1], self.i, self.j)
                movimentos_validos = caminhos > -10

                if npy.sum(self._qMap[estado_atual[0]][estado_atual[1]]) > 0:
                    acao = npy.argmax(self._qMap[estado_atual[0]][estado_atual[1]])
                else:
                    #Primeiras posibilidades de caminhos baseados em Q
                    random.seed()
                    acoes = npy.array(list(range(util_estados.quantidade_acoes())))
                    acoes = acoes[movimentos_validos == True]
                    random.shuffle(acoes)
                    acao = acoes[0]
                    proximo_estado = util_estados.proximo_estado_por_acao(estado_atual, acao, self.i, self.j)
                reward = self.updateQMap(estado_atual, proximo_estado, acao)
                # Estado de 'Goal' 10
                if reward == 10:
                    goal = True
                    break
                estado_atual = proximo_estado    
