import re
import random

from src.funcoes.Moore import MooreMachine


expressaoRegularPadrao = r'^\w'
#leituraMaquinaService = leituraMaquina()

def jogar(maquina1, maquina2, escolha):
    if(escolha == 1):
        moore(maquina1, maquina2)
    if (escolha == 2):
        AFD(maquina1, maquina2)

def getPleam(maquina, numeroTransicao, leitura, estadoAtualMaquina, vidaJogador):
    for i in range(0, len(numeroTransicao)):
        if maquina[f"{estadoAtualMaquina}"][0][i] == leitura and vidaJogador != 0:
            estadoAtualAUX1  = maquina[f"{estadoAtualMaquina}"][1][i]
            pleam = re.search(expressaoRegularPadrao, estadoAtualAUX1)
            pleam = pleam.group()

    return pleam

def rodadaMoore(jogadorAtual, outroJogador, mensagemVidaJogador, mensagemVidaOutroJogador):
    primeiraLetraEstadoJogadorAtual = obterPrimeiraLetraString(jogadorAtual.estadoAtual)
    primeiraLetraEstadoOutroJogador = obterPrimeiraLetraString(outroJogador.estadoAtual)
    mensaguemJogador = ""

    if primeiraLetraEstadoJogadorAtual == "A":
        mensaguemJogador = f"Alcancou um estado de Ataque em {jogadorAtual.nomeJogador}" \
                            f"\nDano no duelista de {outroJogador.nomeJogador}: {jogadorAtual.valorAtributoJogador}"
        mensagemVidaOutroJogador = f"{mensagemVidaOutroJogador} - {jogadorAtual.valorAtributoJogador}"
        outroJogador.vidaAtual -= jogadorAtual.valorAtributoJogador

        if primeiraLetraEstadoOutroJogador == "D":
            mensagemVidaOutroJogador = f"{mensagemVidaOutroJogador} + {outroJogador.valorAtributoJogador}"
            if jogadorAtual.valorAtributoJogador >= outroJogador.valorAtributoJogador:
                outroJogador.vidaAtual += outroJogador.valorAtributoJogador
            else:
                outroJogador.vidaAtual += jogadorAtual.valorAtributoJogador

    elif primeiraLetraEstadoJogadorAtual == "C":
        mensaguemJogador = f"Alcancou um estado de Cura em {jogadorAtual.nomeJogador}" \
                            f"\nCura no duelista de {jogadorAtual.nomeJogador}: {jogadorAtual.valorAtributoJogador}"
        mensagemVidaJogador = f"{mensagemVidaJogador} + {jogadorAtual.valorAtributoJogador}"
        jogadorAtual.vidaAtual += jogadorAtual.valorAtributoJogador

    elif primeiraLetraEstadoJogadorAtual == "D":
        mensaguemJogador = f"Alcancou um estado de Defesa em {jogadorAtual.nomeJogador}" \
                            f"\nAparagem do duelista de {jogadorAtual.nomeJogador}: {jogadorAtual.valorAtributoJogador}"

    return mensagemVidaJogador, mensagemVidaOutroJogador, mensaguemJogador

def obterAtualEstadoJogador(jogadorAtual, numerosTransicao, leitura):
    estadoAtualjogador = None
    for i in range(0, len(numerosTransicao)):
        if jogadorAtual.maquina[f"{jogadorAtual.estadoAtual}"][0][i] == leitura:
            estadoAtualjogador = jogadorAtual.maquina[f"{jogadorAtual.estadoAtual}"][1][i]
    jogadorAtual.estadoAtual = estadoAtualjogador

def moore(maquina1, maquina2):
    jogador1 = MooreMachine("Arazeal", 20, maquina1)
    jogador2 = MooreMachine("Nehrim", 20, maquina2)
    print("\n\n-------------------------------------------------------------------------")
    print(f"Vida do duelista de Arazeal: {jogador1.vida}")
    print(f"Vida do duelista de Nehrim: {jogador2.vida}")

    jogador1.estadoAtual = obterEstadoInicial(maquina1)
    jogador2.estadoAtual = obterEstadoInicial(maquina2)

    turno = 1
    rodadaDoJogador = random.randint(1, 2)
    outroJogador = 0
    numerosTransicao = maquina1["transicao"]

    while True:
        print(f"\n\n->->->          Turno {turno}          <-<-<-")
        if rodadaDoJogador == 1:
            print(f" Turno de {jogador1.nomeJogador} ")
            outroJogador = 2
        else:
            print(f" Turno de {jogador2.nomeJogador} ")
            outroJogador = 1

        leitura = None
        while leitura not in numerosTransicao:
            leitura = int(input("\nQual leitura você deseja fazer?: "))

        jogador1.valorAtributoJogador = random.randint(1, 10)
        obterAtualEstadoJogador(jogador1, numerosTransicao, leitura)
        mensagemVida1 = f"{jogador1.vidaAtual}"

        jogador2.valorAtributoJogador = random.randint(1, 10)
        obterAtualEstadoJogador(jogador2, numerosTransicao, leitura)
        mensagemVida2 = f"{jogador2.vidaAtual}"

        mensagemVida1, mensagemVida2, mensaguemJogador1 = rodadaMoore(jogador1, jogador2, mensagemVida1, mensagemVida2)
        mensagemVida2, mensagemVida1, mensaguemJogador2 = rodadaMoore(jogador2, jogador1, mensagemVida2, mensagemVida1)

        continuar = None
        if rodadaDoJogador == 1:
            if jogador2.vidaAtual <= 0:
                jogador2.vidaAtual = 0
                mensagemVida2 = f"{jogador2.vidaAtual} ({mensagemVida2} = pontos de vida zerados)"
                mensagemVida1 = f"{jogador1.vidaAtual} ({mensagemVida1})"
                continuar = False
            elif jogador1.vidaAtual <= 0:
                jogador1.vidaAtual = 0
                mensagemVida1 = f"{jogador1.vidaAtual} ({mensagemVida1} = pontos de vida zerados)"
                mensagemVida2 = f"{jogador2.vidaAtual} ({mensagemVida2})"
                continuar = False
            else:
                mensagemVida1 = f"{jogador1.vidaAtual} ({mensagemVida1})"
                mensagemVida2 = f"{jogador2.vidaAtual} ({mensagemVida2})"
            print(f"\n{mensaguemJogador1}")
            print(f"\n{mensaguemJogador2}")
            print(f"\nVida restante do duelista de {jogador1.nomeJogador}: {mensagemVida1}")
            print(f"Vida restante do duelista de {jogador2.nomeJogador}: {mensagemVida2}")

            if continuar == False:
                if jogador2.vidaAtual == 0:
                    print(f"{jogador1.nomeJogador} vitorioso!")
                else:
                    print(f"{jogador2.nomeJogador} vitorioso!")
                break
        else:
            if jogador1.vidaAtual <= 0:
                jogador1.vidaAtual = 0
                mensagemVida1 = f"{jogador1.vidaAtual} ({mensagemVida1} = pontos de vida zerados)"
                mensagemVida2 = f"{jogador2.vidaAtual} ({mensagemVida2})"
                continuar = False

            elif jogador2.vidaAtual <= 0:
                jogador2.vidaAtual = 0
                mensagemVida2 = f"{jogador2.vidaAtual} ({mensagemVida2} = pontos de vida zerados)"
                mensagemVida1 = f"{jogador1.vidaAtual} ({mensagemVida1})"
                continuar = False
            else:
                mensagemVida1 = f"{jogador1.vidaAtual} ({mensagemVida1})"
                mensagemVida2 = f"{jogador2.vidaAtual} ({mensagemVida2})"
            print(f"\n{mensaguemJogador2}")
            print(f"\n{mensaguemJogador1}")
            print(f"\nVida restante do duelista de {jogador2.nomeJogador}: {mensagemVida2}")
            print(f"Vida restante do duelista de {jogador1.nomeJogador}: {mensagemVida1}")
            if continuar == False:
                if jogador1.vidaAtual == 0:
                    print(f"{jogador2.nomeJogador} vitorioso!")
                else:
                    print(f"{jogador1.nomeJogador} vitorioso!")
                break

        aux = outroJogador
        outroJogador = rodadaDoJogador
        rodadaDoJogador = aux
        turno += 1



def rodadaADF(numeroTransicao, maquina1, maquina2, duelista1, duelista2, vidaJogador1, vidaJogador2, quemJoga, outroJogador, leitura, estadoAtualMaquina1, estadoAtualMaquina2, estadoAtualAUX1, estadoAtualAUX2, count):
    pleam1 = getPleam(maquina1, numeroTransicao, leitura, estadoAtualMaquina1, vidaJogador1)
    pleam2 = getPleam(maquina2, numeroTransicao, leitura, estadoAtualMaquina2, vidaJogador2)

    valorAtributoJogador1 = random.randint(1, 10)
    valorAtributoJogador2 = random.randint(1, 10)
    vida1 = f"{vidaJogador1}"
    vida2 = f"{vidaJogador2}"
    mensaguemJogador1 = ""
    mensaguemJogador2 = ""

    if vidaJogador1 == 0:
        mensaguemJogador1 = f"O duelista de {duelista1} morreu. Nao sera feita nenhuma acao mais"
    elif pleam1 != "E" and pleam1 != "F":
        estadoAtualMaquina1 = estadoAtualAUX1
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

        elif pleam1 == "C":
            mensaguemJogador1 = f"Alcancou um estado de Cura em {duelista1}" \
                                f"\nCura no duelista de {duelista1}: {valorAtributoJogador1}"
            vida1 = f"{vida1} + {valorAtributoJogador1}"
            vidaJogador1 += valorAtributoJogador1

        elif pleam1 == "D":
            mensaguemJogador1 = f"Alcancou um estado de Defesa em {duelista1}" \
                            f"\nAparagem do duelista de {duelista1}: {valorAtributoJogador1}"
    elif pleam1 == "E":
        mensaguemJogador1 = f"Alcancou um estado de ERRO em {duelista1}. " \
                            f"Punicao!!!: Nenhuma acao do duelista de {duelista1} sera feita no turno {count}"
    elif pleam1 == "F":
        estadoAtualMaquina1 = estadoAtualAUX1
        mensaguemJogador1 = f"O {duelista1} alcancou o estado final."

    if vidaJogador2 == 0:
        mensaguemJogador2 = f"O duelista de {duelista2} morreu. Nao sera feita nenhuma acao mais"
    if pleam2 != "E" and pleam2 != "F":
        estadoAtualMaquina2 = estadoAtualAUX2
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

        elif pleam2 == "C":
            mensaguemJogador2 = f"Alcancou um estado de Cura em {duelista2}" \
                                f"\nCura no duelista de {duelista2}: {valorAtributoJogador2}"
            vida2 = f"{vida2} + {valorAtributoJogador2}"
            vidaJogador2 += valorAtributoJogador2

        elif pleam2 == "D":
            mensaguemJogador2 = f"Alcancou um estado de Defesa em {duelista2}" \
                                f"\nAparagem do duelista de {duelista2}: {valorAtributoJogador2}"
    elif pleam2 == "E":
        mensaguemJogador2 = f"Alcancou um estado de ERRO em {duelista2}. " \
                            f"Punicao!!! : Nenhuma acao do duelista de {duelista2} sera feita no turno {count}"
    elif pleam2 == "F":
        estadoAtualMaquina2 = estadoAtualAUX2
        mensaguemJogador2 = f"O {duelista2} alcancou o estado final."

    if vidaJogador1 <= 0:
        vidaJogador1 = 0
        vida1 = f"{vidaJogador1} ({vida1} = pontos de vida zerados)"
        vida2 = f"{vidaJogador2} ({vida2})"
    elif vidaJogador2 <= 0:
        vidaJogador2 = 0
        vida2 = f"{vidaJogador2} ({vida2} = pontos de vida zerados)"
        vida1 = f"{vidaJogador1} ({vida1})"
    else:
        vida1 = f"{vidaJogador1} ({vida1})"
        vida2 = f"{vidaJogador2} ({vida2})"

    if quemJoga == 1:
        print(f"\n{mensaguemJogador1}")
        print(f"\n{mensaguemJogador2}")
        print(f"\nVida restante do duelista de {duelista1}: {vida1}")
        print(f"Vida restante do duelista de {duelista2}: {vida2}")
    else:
        print(f"\n{mensaguemJogador2}")
        print(f"\n{mensaguemJogador1}")
        print(f"\nVida restante do duelista de {duelista2}: {vida2}")
        print(f"Vida restante do duelista de {duelista1}: {vida1}")


def AFD(maquina1, maquina2):
    print(f"-------------------------     ENTREI AFD     -------------------------")
    vidaJogador1 = random.randint(0, 100)
    vidaJogador2 = vidaJogador1
    print(f"Vida do duelista de Arazeal: {vidaJogador1}")
    print(f"Vida do duelista de Nehrim: {vidaJogador2}")

    estadoAtualMaquina1, estadoAtualMaquina2 = obterEstadoInicial(maquina1, maquina2)
    estadoAtualAUX1 = estadoAtualAUX2 = None
    count = 1
    duelista1 = "Arazeal"
    duelista2 = "Nehrim"
    quemJoga = random.randint(1, 2)
    outroJogador = 0
    numeroTransicao = maquina1["transicao"]

    while True:
        print(f"\n\n->->->          Turno {count}          <-<-<-")
        pleam1 = "Z"  # primeira letra do estado atual da maquina 1
        pleam2 = "Z"  # primeira letra do estado atual da maquina 2
        if quemJoga == 1 and vidaJogador1 != 0:
            print(f" Turno de {duelista1} ")
            outroJogador = 2
        elif quemJoga == 2 and vidaJogador2 != 0:
            print(f" Turno de {duelista2} ")
            outroJogador = 1
        elif quemJoga == 1 and vidaJogador1 == 0:
            print(f"O duelista do jogador {duelista1} morreu. Dessa forma o turno passou para {duelista2}")
            quemJoga = 2
            outroJogador = 1
        elif quemJoga == 2 and vidaJogador2 == 0:
            print(f"O duelista do jogador {duelista2} morreu. Dessa forma o turno passou para {duelista1}")
            quemJoga = 1
            outroJogador = 2

        leitura = None
        while leitura not in numeroTransicao:
            leitura = int(input("\nQual leitura você deseja fazer?: "))

        vidaJogador1, vidaJogador2, estadoAtualMaquina1, estadoAtualMaquina2, estadoAtualAUX1, estadoAtualAUX2 = rodadaADF(numeroTransicao, maquina1, maquina2, duelista1, duelista2, vidaJogador1, vidaJogador2, quemJoga, outroJogador, leitura, estadoAtualMaquina1, estadoAtualMaquina2, estadoAtualAUX1, estadoAtualAUX2, count)
        
        if pleam1 == "F" and pleam2 == "F":
            if vidaJogador1 < vidaJogador2:
                print(f"{duelista2} vitorioso!")
            elif vidaJogador1 > vidaJogador2:
                print(f"{duelista1} vitorioso!")
            elif vidaJogador1 == vidaJogador2:
                print(f"O {duelista1} e o {duelista2} empataram a partida")
            break
        elif pleam1 == "F":
            print(f"{duelista1} vitorioso!")
            break
        elif pleam2 == "F":
            print(f"{duelista2} vitorioso!")
            break

        aux = outroJogador
        outroJogador = quemJoga
        quemJoga = aux
        count += 1

def obterPrimeiraLetraString(string):
    primeiraLetra = re.search(expressaoRegularPadrao, string)
    primeiraLetra = primeiraLetra.group()
    return primeiraLetra

def obterEstadoInicial(maquina):
    keysMaquina = maquina.keys()
    keysMaquina = list(keysMaquina)
    estadoInicialMaquina = None
    for key in keysMaquina:
        primeiraLetra = obterPrimeiraLetraString(key)
        if(primeiraLetra == "I"):
            estadoInicialMaquina = key
            break
    return estadoInicialMaquina


def leituraArquivo(filename):
    maquina = dict()
    with open(filename, 'r') as file:
        content = file.read().rstrip('\n')
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
