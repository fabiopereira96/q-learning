# -*- coding: utf-8 -*-
from qlearning import Qlearning
import sys
import time
import timeit
import util_file
import util_estados
import numpy as np

def main(sys):
	if len(sys.argv) == 5:
		print(sys.argv)
		dados = util_file.f_read(sys.argv[1])
		x = sys.argv[2]
		y= sys.argv[3]
		n = sys.argv[4]
		i = int(dados[0])
		j = int(dados[1])
		mapa = dados[2]
		ql = Qlearning(mapa, i, j, x, y, n)
		ql.setPiMap(ql.getOMap())
		ql.calculateInitialQMap()
		ql.executeQLearning()
		ql.fiilPiMap()
		util_file.f_write(ql.getPiMap(), "pi.txt", ql.getQMap(), "q.txt")
		print("Finish.")
	else:
		print( "Entrada invalida. Padrão aceito: mapa x y n")

main(sys)

