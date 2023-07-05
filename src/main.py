import funcoes
import re
import random
expressaoRegularPadrao = r'^\w'

def main():

    maquina1 = funcoes.leituraArquivo('teste/AFD_10.txt')
    maquina2 = funcoes.leituraArquivo('teste/AFD_20.txt')
    #funcoes.jogar(maquina1, maquina2, escolha)
    #print(maquina1)
    funcoes.executaBatalha(maquina1, maquina2)

if __name__ == "__main__":
    main()
