# -*- coding: utf-8 -*-
import util_estados
import numpy as npy

def r_file(file_map):
    data = []
    mapa = []
    k = 0
    for linha in file_map:
        if k == 0:
            ad_map = linha
        else:
            data.append(linha.split())
        k += 1
    i = ad_map.split()[0]
    j = ad_map.split()[1]
    k = i
    for lin in range(0, int(i)):
        mapa.append(list(data[lin][0]))

    file_map.close()
    return [i, j, mapa]
    
#Lê o arquivo contendo mapa à ser analisado
# return [linha, coluna, mapa, estado_inicial, estado_final]
def f_read(file_dir):
    #Lê as informações do arquivo .txt
    #e salva numa mapa
    file_map = open(file_dir, "r")
    dados = r_file(file_map)
    return dados #[linha, coluna, mapa]
#end read_file

def f_write(pi_mapa, pi_dir, q_mapa, q_dir):
    pi_file = open(pi_dir, "w")
    q_file = open(q_dir, "w")
    texto = []
    print(pi_mapa)
    i, j = npy.shape(pi_mapa)
    for col in range(0, int(j)):
        texto = " ".join(str(x) for x in pi_mapa[col]) + '\n'
        pi_file.write(texto)



