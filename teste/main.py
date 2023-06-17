import funcoes

def main():

    maquina1 = funcoes.leituraArquivoMoore('teste/arquivoTeste1.txt')
    maquina2 = funcoes.leituraArquivoMoore('teste/arquivoTeste2.txt')
    escolha = 1 # Para escolher qual tipo de maquina, por enquanto so de moore

    #funcoes.jogar(maquina1, maquina2, escolha)

if __name__ == "__main__":
    main()
