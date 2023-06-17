import re
import random
expressaoRegularPadrao = r'^\w'

def jogar(maquina1, maquina2, escolha):
    if(escolha == 1):
        moore(maquina1, maquina2)

def moore(maquina1, maquina2):
    vidaJogador1 = random.randint(0, 100)
    vidaJogador2 = vidaJogador1
    print(f"Vida do duelista de Arazeal: {vidaJogador1}")
    print(f"Vida do duelista de Nehrim: {vidaJogador2}")

    estadoAtualMaquina1 , estadoAtualMaquina2 = obterEstadoInicial(maquina1, maquina2)

    count = 1
    duelista1 = "Arazeal"
    duelista2 = "Nehrim"
    quemJoga = random.randint(1, 2)
    outroJogador = 0
    numeroTransicao = maquina1["transicao"]
    while vidaJogador1 > 0 or vidaJogador2 > 0:
        print(f"\n\n->->->          Turno {count}          <-<-<-")
        if quemJoga == 1:
            print(f" Turno de {duelista1} ")
            outroJogador = 2
        else:
            print(f" Turno de {duelista2} ")
            outroJogador = 1

        leitura = None
        while leitura not in numeroTransicao:
            leitura = int(input("\nQual leitura você deseja fazer?: "))

        for i in range(0, len(numeroTransicao)):
            if maquina1[f"{estadoAtualMaquina1}"][0][i] == leitura:
                estadoAtualMaquina1 = maquina1[f"{estadoAtualMaquina1}"][1][i]
            if maquina2[f"{estadoAtualMaquina2}"][0][i] == leitura:
                estadoAtualMaquina2 = maquina2[f"{estadoAtualMaquina2}"][1][i]

        pleam1 = "" # primeira letra do estado atual da maquina 1
        pleam2 = "" # primeira letra do estado atual da maquina 2
        pleam1 = re.search(expressaoRegularPadrao, estadoAtualMaquina1)
        pleam1 = pleam1.group()
        pleam2 = re.search(expressaoRegularPadrao, estadoAtualMaquina2)
        pleam2 = pleam2.group()

        valorAtributoJogador1 = random.randint(1, 10)
        valorAtributoJogador2 = random.randint(1, 10)
        vida1 = f"{vidaJogador1}"
        vida2 = f"{vidaJogador2}"
        mensaguemJogador1 = ""
        mensaguemJogador2 = ""
        continuar = True

        if pleam1 == "A":
            mensaguemJogador1 = f"Alcancou um estado de Ataque em {duelista1}" \
                                f"\nDano no duelista de {duelista2}: {valorAtributoJogador1}"
            vida2 = f"{vida2} - {valorAtributoJogador1}"
            vidaJogador2 -= valorAtributoJogador1
            if pleam2 == "D":
                vida2 = f"{vida2} + {valorAtributoJogador2}"
                if valorAtributoJogador1 >= valorAtributoJogador2:
                    vidaJogador2 += valorAtributoJogador2
                else:
                    vidaJogador2 += valorAtributoJogador1

            if vidaJogador2 <= 0:
                vidaJogador2 = 0
                vida2 = f"{vidaJogador2} ({vida2} = pontos de vida zerados)"
                vida1 = f"{vidaJogador1} ({vida1})"
                continuar = False

        elif pleam1 == "C":
            mensaguemJogador1 = f"Alcancou um estado de Cura em {duelista1}" \
                                f"\nCura no duelista de {duelista1}: {valorAtributoJogador1}"
            vida1 = f"{vida1} + {valorAtributoJogador1}"
            vidaJogador1 += valorAtributoJogador1


        if pleam2 == "A":
            mensaguemJogador2 = f"Alcancou um estado de Ataque em {duelista2}" \
                                f"\nDano no duelista de {duelista1}: {valorAtributoJogador2}"
            vida1 = f"{vida1} - {valorAtributoJogador2}"
            vidaJogador1 -= valorAtributoJogador2
            if pleam1 == "D":
                vida1 = f"{vida1} + {valorAtributoJogador1}"
                if valorAtributoJogador2 >= valorAtributoJogador1:
                    vidaJogador1 += valorAtributoJogador1
                else:
                    vidaJogador1 += valorAtributoJogador2

            if vidaJogador1 <= 0:
                vidaJogador1 = 0
                vida1 = f"{vidaJogador1} ({vida1} = pontos de vida zerados)"
                vida2 = f"{vidaJogador2} ({vida2})"
                continuar = False

        elif pleam2 == "C":
            mensaguemJogador2 = f"Alcancou um estado de Cura em {duelista2}" \
                                f"\nCura no duelista de {duelista2}: {valorAtributoJogador2}"
            vida2 = f"{vida2} + {valorAtributoJogador2}"
            vidaJogador2 += valorAtributoJogador2

        if pleam1 == "D":
            mensaguemJogador1 = f"Alcancou um estado de Defesa em {duelista1}" \
                                f"\nAparagem do duelista de {duelista1}: {valorAtributoJogador1}"

        if pleam2 == "D":
            mensaguemJogador2 = f"Alcancou um estado de Defesa em {duelista2}" \
                                f"\nAparagem do duelista de {duelista2}: {valorAtributoJogador2}"
        if continuar == True:
            vida1 = f"{vidaJogador1} ({vida1})"
            vida2 = f"{vidaJogador2} ({vida2})"
        if quemJoga == 1:
            print(f"\n{mensaguemJogador1}")
            print(f"\n{mensaguemJogador2}")
        else:
            print(f"\n{mensaguemJogador2}")
            print(f"\n{mensaguemJogador1}")

        print(f"\nVida restante do duelista de {duelista1}: {vida1}")
        print(f"Vida restante do duelista de {duelista2}: {vida2}")
        if continuar == False:
            if vidaJogador1 == 0:
                print(f"{duelista2} vitorioso!")
            else:
                print(f"{duelista1} vitorioso!")
            break
        aux = outroJogador
        outroJogador = quemJoga
        quemJoga = aux
        count += 1

def obterEstadoInicial(maquina1, maquina2):
    keysMaquina1 = maquina1.keys()
    keysMaquina2 = maquina2.keys()
    keysMaquina1 = list(keysMaquina1)
    keysMaquina2 = list(keysMaquina2)
    estadoInicialMaquina1 = ""
    estadoInicialMaquina2 = ""
    for key in keysMaquina1:
        primeiraLetra = re.search(expressaoRegularPadrao, key)
        primeiraLetra = primeiraLetra.group()
        if(primeiraLetra == "I"):
            estadoInicialMaquina1 = key
    for key in keysMaquina2:
        primeiraLetra = re.search(expressaoRegularPadrao, key)
        primeiraLetra = primeiraLetra.group()
        if(primeiraLetra == "I"):
            estadoInicialMaquina2 = key
    return estadoInicialMaquina1, estadoInicialMaquina2


def leituraArquivoMoore(filename):
    maquina = dict()
    with open(filename, 'r') as file:
        content = file.read()
    lines = content.split('\n')
    Q = lines[0].split(" ")[1:]
    maquina["transicao"] = list[int]()
    for estado in Q:
        maquina[f"{estado}"] = [[], []]
    for i in range(2, len(lines)):
        transicao = lines[i]
        transicao = transicao.split(" -> ")
        estadoOrigem = transicao[0]
        transicao = transicao[1]
        transicao = transicao.split(" | ")
        estadoDestino = transicao[0]
        transicao = transicao[1].split(" ")
        transicao = list(map(int, transicao))
        for numeroFazTransicao in transicao:
            maquina[f"{estadoOrigem}"][0].append(numeroFazTransicao)
            maquina[f"{estadoOrigem}"][1].append(estadoDestino)
            if numeroFazTransicao not in maquina["transicao"]:
                maquina["transicao"].append(numeroFazTransicao)

    return maquina
