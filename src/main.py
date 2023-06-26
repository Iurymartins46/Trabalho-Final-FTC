import funcoes

def main():
    escolha = None # Para escolher qual tipo de maquina: 1 = de moore; 2 = AFD
    while escolha not in [1, 2]:
        print("\nQual tipo de maquina deseja ultilizar:\n1 para moore\n2 para AFD")
        escolha = int(input("Qual sua escolha: "))
    #maquina1 = funcoes.leituraArquivoMoore('teste/maquinaMoore01.txt')
    #maquina2 = funcoes.leituraArquivoMoore('teste/maquinaMoore02.txt')
    maquina1 = funcoes.leituraArquivoMoore('teste/maquinaAFD01.txt')
    maquina2 = funcoes.leituraArquivoMoore('teste/maquinaAFD02.txt')
    funcoes.jogar(maquina1, maquina2, escolha)

if __name__ == "__main__":
    main()
