import funcoes
import re
import random
expressaoRegularPadrao = r'^\w'

def main():
    """escolha = None # Para escolher qual tipo de maquina: 1 = de moore; 2 = AFD
    while escolha not in [1, 2]:
        print("\nQual tipo de maquina deseja ultilizar:\n1 para moore\n2 para AFD")
        escolha = int(input("Qual sua escolha: "))"""
    #maquina1 = funcoes.leituraArquivo('../teste/maquinaMoore01.txt')
    maquina2 = funcoes.leituraArquivo('../teste/maquinaMoore02.txt')
    maquina1 = funcoes.leituraArquivo('../teste/maquinaAFD01.txt')
    #maquina2 = funcoes.leituraArquivo('../teste/maquinaAFD02.txt')
    #funcoes.jogar(maquina1, maquina2, escolha)

    funcoes.executaBatalha(maquina1, maquina2)

if __name__ == "__main__":
    main()
