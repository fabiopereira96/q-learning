# -*- coding: utf-8 -*-
import sys
import numpy as npy
from random import randrange
#Retorna o valor considerado como "parade" para
#a busca dos caminhos disponíveis.
#return @
def wall():
    return '#'

def cost_by_content(content):
	cost = {'0': 10, '-': -1, '&': -10, '#': -1}
	return int(cost[content])

def quantidade_acoes():
	return 4

def mapea_acao(acao, chave):
	mapaAcao = [[{"nome":"acima", "simbolo": "^"}],
				[{"nome":"esquerda", "simbolo": "<"}],
				[{"nome":"abaixo", "simbolo": "v"}], 
				[{"nome":"direita", "simbolo": ">"}]]
	return mapaAcao[acao][0][chave]

# Dada um mapa e o estado atual pelas coordenadas (m,n),
# encontra as ramificações possíveis de (m,n)
#return array ramificações
#Ordem-> sobe, esquerda, desce, direita
def ramifica_estado(mapa, i, j, M, N):
	
	ramos = [] #Inicia lista de ramos
	#Sobe
	if i > 0 and mapa[i-1][j] != wall():
		ramos.append(costByContent(mapa[i-1][j]))
	else:
		ramos.append(costByContent(wall()))
	#Esquerda
	if j > 0 and mapa[i][j-1] != wall():
		ramos.append(costByContent(mapa[i][j-1]))
	else:
		ramos.append(costByContent(wall()))
	#Desce
	if i+1 < M and mapa[i+1][j] != wall():
		ramos.append(costByContent(mapa[i+1][j]))
	else:
		ramos.append(costByContent(wall()))
	#Direita
	if j+1 < N and mapa[i][j+1] != wall():
		ramos.append(costByContent(mapa[i][j+1]))
	else:
		ramos.append(costByContent(wall()))
	
	return npy.array(ramos)  # Lista de movimentos possíveis

def proximo_estado_por_acao(estado_atual, acao, M, N):
	proximo_estado = []	
	i = estado_atual[0]
	j = estado_atual[1]
	if acao == 0:
		if i > 0:
			proximo_estado = [i-1, j]
	elif acao == 1:
		if i+1 < M:
			proximo_estado = [i+1, j]
	elif acao == 2:
		if j > 0:
			proximo_estado = [i, j-1]
	elif acao == 3:
		if j+1 < N:
			proximo_estado = [i, j+1]

	if not proximo_estado:
		proximo_estado = [i, j]
	return proximo_estado


def cria_estado_aleatorio(i, j):
	x = randrange(0, int(i))
	y = randrange(0, int(j))
	return [x, y]

