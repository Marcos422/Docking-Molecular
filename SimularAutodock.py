# -*- coding: utf-8 -*-
"""
Programa para fazer simulações com o AutoDock Vina
O arquivo SimularAutodock.py deve ficar na mesma pasta que o ligante, receptor, config.txt e o arquivo "vina.exe".
"""
import time
from subprocess import *
import os

def main():
    dirNome = 'Resultados'
    if not os.path.exists(dirNome): #Cria uma pasta Resultados para depositar os resultados do Docking
        os.mkdir(dirName)
        print("Diretório " , dirNome ,  " criado.")
    else:    
        print("Diretório " , dirNome ,  " já existe.")
    print('=-'*30)
    print('Simulações de diversas posições com AutodockVina.')
    print('Edite o programa no seu editor de Python antes de usa-lo.')
    print('Certifique-se de executar apenas o arquivo "SimularAutodock.py" quando for rodar o programa')
    print('=-'*30)
    insert = input('Tecle ENTER para começar')
    calc_pos()
    print('Copie M')
    insert = input('Tecle ENTER para finalizar')
def calc_pos():
    t0 = time.perf_counter() #Conta o tempo de execucao do programa
    x0, y0, z0 = 0, -8, 10
    x1, y1, z1 = 15, 2, 18
    pulo = 5 #O programa começa na posicao [x0, y0, z0] depois [x0, y0, z0 + pulo], e assim por diante...
    '''IMPORTANTE como se trata de muitas execuções do 
    Vina entre com um intervalo entre as simulações. Isso pode ser feito calculando o tempo de uma simulação completa.
    Assim evita-se o risco do computador travar devido a processos simultâneos no processador.'''

    for i in range(x0, x1+1, 3): 
        for j in range(y0, y1+1, 2):
            for k in range(z0, z1+1, 2):
                Popen('cmd /k "vina.exe" --config config.txt --center_x '+ str(i)+' --center_y '+ str(j)+' --center_z '+ str(k)+
                  ' --out Resultados\proteina-ligante,'+str(i)+','+str(j)+','+str(k)+',.pdbqt --log Resultados\log,'+str(i)+','+str(j)+','+str(k)+',.txt')
                """
                Adiciona as posicoes do teste na lista M para um uso posterior.
                Executa o cmd e digita o seguinte comando no terminal
                "vina.exe" --config config.txt --center_x [pos_x] --center_y [pos_y] -- center_z [pos_z]
                --out proteina-ligante[pos_x][pos_y][pos_z].pdbqt --log log[pos_x][pos_y][pos_z].txt
                """
                time.sleep(15)
    time.sleep(5)
    print('Terminou! \nTempo de excução: {} s'.format(time.perf_counter() - t0))
    file = open("M.txt", "w") 
    file.write(str(M)) 
    file.close()
    print('Foi criado um arquivo chamado M contendo todas as posições simuladas pelo Vina.')



if __name__ == '__main__':
    main()
