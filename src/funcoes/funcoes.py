import re
import random

expressaoRegularPadrao = r'^\w'

from funcoes.Maquina import Machine


def executaBatalha(maquina1, maquina2):
    jogador1 = Machine("Russia", 20, maquina1)
    jogador2 = Machine("Ucrania", 12, maquina2)
    print("\n\n-------------------------------------------------------------------------")
    print(f"Vida do duelista de Russia: {jogador1.vida}")
    print(f"Vida do duelista de Ucrania: {jogador2.vida}")

    jogador1.estadoAtual = obterEstadoInicial(maquina1)
    jogador2.estadoAtual = obterEstadoInicial(maquina2)

    turno = 1
    rodadaDoJogador = random.randint(1, 2)
    outroJogador = 0
    numerosTransicao = maquina1["transicao"]

    jogadaJogador1Executar = True
    jogadaJogador2Executar = True

    while True:
        print(f"\n\n->->->          Turno {turno}          <-<-<-")
        mensagemVidaJogador1 = mensagemVidaJogador2 = ""

        if rodadaDoJogador == 1:
            if jogador2.vidaAtual == 0:
                mensaguemJogador2 = f"O duelista de {jogador2.nomeJogador} morreu. Nao sera feita nenhuma acao para este jogador."
            if jogador1.vidaAtual == 0:
                mensaguemJogador1 = f"O duelista de {jogador1.nomeJogador} morreu. Nao sera feita nenhuma acao para este jogador\n"
                print(f"Turno passa para o jogador {jogador2.nomeJogador} ")
            else:
                print(f"Turno de {jogador1.nomeJogador} ")
            outroJogador = 2
        else:
            if jogador1.vidaAtual == 0:
                mensaguemJogador1 = f"O duelista de {jogador1.nomeJogador} morreu. Nao sera feita nenhuma acao para este jogador."
            if jogador2.vidaAtual == 0:
                mensaguemJogador2 = f"O duelista de {jogador2.nomeJogador} morreu. Nao sera feita nenhuma acao para este jogador."
                print(f"Turno passa para o jogador {jogador1.nomeJogador} ")
            else:
                print(f" Turno de {jogador2.nomeJogador} ")
            outroJogador = 1

        leitura = None
        while leitura not in numerosTransicao:
            leitura = int(input("\nQual leitura você deseja fazer?: "))

        jogador1.valorAtributoJogador = random.randint(1, 10)
        proximoEstadoJogador1 = obterAtualEstadoJogador(jogador1, leitura)
        mensagemVidaJogador1 = f"{jogador1.vidaAtual}"

        jogador2.valorAtributoJogador = random.randint(1, 10)
        proximoEstadoJogador2 = obterAtualEstadoJogador(jogador2, leitura)
        mensagemVidaJogador2 = f"{jogador2.vidaAtual}"

        if rodadaDoJogador == 1:
            if jogadaJogador1Executar == True:
                mensagemVidaJogador1, mensagemVidaJogador2, mensaguemJogador1 = executaJogada(jogador1, jogador2, mensagemVidaJogador1,
                                                                            mensagemVidaJogador2, proximoEstadoJogador1, proximoEstadoJogador2, turno)
            if jogadaJogador2Executar == True:
                mensagemVidaJogador2, mensagemVidaJogador1, mensaguemJogador2 = executaJogada(jogador2, jogador1, mensagemVidaJogador2,
                                                                            mensagemVidaJogador1, proximoEstadoJogador2, proximoEstadoJogador1, turno)
            if jogador1.vidaAtual == 0:
                jogadaJogador1Executar = False
            if jogador2.vidaAtual == 0:
                jogadaJogador2Executar = False

        else:
            if jogadaJogador2Executar == True:
                mensagemVidaJogador2, mensagemVidaJogador1, mensaguemJogador2 = executaJogada(jogador2, jogador1, mensagemVidaJogador2,
                                                                            mensagemVidaJogador1, proximoEstadoJogador2, proximoEstadoJogador1, turno)
            if jogadaJogador1Executar == True:
                mensagemVidaJogador1, mensagemVidaJogador2, mensaguemJogador1 = executaJogada(jogador1, jogador2, mensagemVidaJogador1,
                                                                            mensagemVidaJogador2, proximoEstadoJogador1, proximoEstadoJogador2, turno)
            if jogador1.vidaAtual == 0:
                jogadaJogador1Executar = False
            if jogador2.vidaAtual == 0:
                jogadaJogador2Executar = False

        continuar = None
        if rodadaDoJogador == 1:
            mensagemVidaJogador1, mensagemVidaJogador2 = construirMesgemVida(jogador1, jogador2, mensagemVidaJogador1, mensagemVidaJogador2)

            print(f"\n{mensaguemJogador1}")
            print(f"\n{mensaguemJogador2}")
            print(f"\nVida restante do duelista de {jogador1.nomeJogador}: {mensagemVidaJogador1}")
            print(f"Vida restante do duelista de {jogador2.nomeJogador}: {mensagemVidaJogador2}")

            continuar = condicaoParada(jogador1, jogador2)

        else:
            mensagemVidaJogador2, mensagemVidaJogador1 = construirMesgemVida(jogador2, jogador1, mensagemVidaJogador2, mensagemVidaJogador1)

            print(f"\n{mensaguemJogador2}")
            print(f"\n{mensaguemJogador1}")
            print(f"\nVida restante do duelista de {jogador2.nomeJogador}: {mensagemVidaJogador2}")
            print(f"Vida restante do duelista de {jogador1.nomeJogador}: {mensagemVidaJogador1}")

            continuar = condicaoParada(jogador2, jogador1)

        if continuar == False:
            break
        aux = outroJogador
        outroJogador = rodadaDoJogador
        rodadaDoJogador = aux
        turno += 1

def executaJogada(jogadorAtual, outroJogador, mensagemVidaJogador, mensagemVidaOutroJogador, proximoEstadoJogador, proximoEstadoOutroJogador , turno):
    mensaguemJogador = ""
    pleaJogadorAtual = obterPrimeiraLetraString(proximoEstadoJogador)  # Primeira letra do estado atual do jogador
    pleaOutroJogador = obterPrimeiraLetraString(proximoEstadoOutroJogador)  # Primeira letra do estado atual do outro jogador
    mensaguemJogador = ""

    if pleaJogadorAtual != "E" and pleaJogadorAtual != "F":
        jogadorAtual.estadoAtual = proximoEstadoJogador
        if pleaJogadorAtual == "A":
            mensaguemJogador = f"Alcancou um estado de Ataque em {jogadorAtual.nomeJogador}" \
                               f"\nDano no duelista de {outroJogador.nomeJogador}: {jogadorAtual.valorAtributoJogador}"
            mensagemVidaOutroJogador = f"{mensagemVidaOutroJogador} - {jogadorAtual.valorAtributoJogador}"
            outroJogador.vidaAtual -= jogadorAtual.valorAtributoJogador

            if pleaOutroJogador == "D":
                mensagemVidaOutroJogador = f"{mensagemVidaOutroJogador} + {outroJogador.valorAtributoJogador}"
                if jogadorAtual.valorAtributoJogador >= outroJogador.valorAtributoJogador:
                    outroJogador.vidaAtual += outroJogador.valorAtributoJogador
                else:
                    outroJogador.vidaAtual += jogadorAtual.valorAtributoJogador
            if outroJogador.vidaAtual <= 0:
                outroJogador.vidaAtual = 0

        elif pleaJogadorAtual == "C":
            mensaguemJogador = f"Alcancou um estado de Cura em {jogadorAtual.nomeJogador}" \
                               f"\nCura no duelista de {jogadorAtual.nomeJogador}: {jogadorAtual.valorAtributoJogador}"
            mensagemVidaJogador = f"{mensagemVidaJogador} + {jogadorAtual.valorAtributoJogador}"
            jogadorAtual.vidaAtual += jogadorAtual.valorAtributoJogador

        elif pleaJogadorAtual == "D":
            mensaguemJogador = f"Alcancou um estado de Defesa em {jogadorAtual.nomeJogador}" \
                               f"\nAparagem do duelista de {jogadorAtual.nomeJogador}: {jogadorAtual.valorAtributoJogador}"

    elif pleaJogadorAtual == "E":
        mensaguemJogador = f"Alcancou um estado de ERRO em {jogadorAtual.nomeJogador}. " \
                           f"Punicao!!!: Nenhuma acao do duelista de {jogadorAtual.nomeJogador} sera feita no turno {turno}"

    elif pleaJogadorAtual == "F":
        jogadorAtual.estadoAtual = proximoEstadoJogador
        mensaguemJogador = f"O {jogadorAtual.nomeJogador} alcancou o estado final."

    return mensagemVidaJogador, mensagemVidaOutroJogador, mensaguemJogador

def construirMesgemVida(jogadorAtual, outroJogador, mensagemVidaJogador, mensagemVidaOutroJogador):
    if outroJogador.vidaAtual == 0:
        mensagemVidaJogador = f"{jogadorAtual.vidaAtual} ({mensagemVidaJogador})"
        mensagemVidaOutroJogador = f"{outroJogador.vidaAtual} ({mensagemVidaOutroJogador} = pontos de vida zerados)"
    elif jogadorAtual.vidaAtual == 0:
        mensagemVidaJogador = f"{jogadorAtual.vidaAtual} ({mensagemVidaJogador} = pontos de vida zerados)"
        mensagemVidaOutroJogador = f"{outroJogador.vidaAtual} ({mensagemVidaOutroJogador})"
    else:
        mensagemVidaJogador = f"{jogadorAtual.vidaAtual} ({mensagemVidaJogador})"
        mensagemVidaOutroJogador = f"{outroJogador.vidaAtual} ({mensagemVidaOutroJogador})"
    return mensagemVidaJogador, mensagemVidaOutroJogador

def maquinaTemEstadoFinal(jogador):
    keysMaquina = jogador.maquina.keys()
    keysMaquina = list(keysMaquina)
    for key in keysMaquina:
        primeiraLetra = obterPrimeiraLetraString(key)
        if (primeiraLetra == "F"):
            return True
    return False

def condicaoParada(jogadorAtual, outroJogador):
    maquina1TemEstadoFinal = maquinaTemEstadoFinal(jogadorAtual)
    maquina2TemEstadoFinal = maquinaTemEstadoFinal(outroJogador)
    pleaJogadorAtual = obterPrimeiraLetraString(jogadorAtual.estadoAtual)  # Primeira letra do estado atual do jogador
    pleaOutroJogador = obterPrimeiraLetraString(outroJogador.estadoAtual)  # Primeira letra do estado atual do outro jogador

    if maquina1TemEstadoFinal == True and maquina2TemEstadoFinal == True:
        if pleaJogadorAtual == "F":
            print(f"{jogadorAtual.nomeJogador} vitorioso!")
            return False
        elif pleaOutroJogador == "F":
            print(f"{outroJogador.nomeJogador} vitorioso!")
            return False
        elif jogadorAtual.vidaAtual == 0 and outroJogador.vidaAtual == 0:
            print(f"Tanto o jogador {jogadorAtual.nomeJogador} quanto {outroJogador.nomeJogador} morreram antes de "
                  f"chegarem ao estado final. Dessa forma nao ouve ganhador")
            return False
    elif outroJogador.vidaAtual == 0 or pleaJogadorAtual == "F":
        print(f"{jogadorAtual.nomeJogador} vitorioso!")
        return False
    elif jogadorAtual.vidaAtual == 0 or pleaOutroJogador == "F":
        print(f"{outroJogador.nomeJogador} vitorioso!")
        return False
    return True

def obterAtualEstadoJogador(jogadorAtual, leitura):
    estadoAtualjogador = list()
    for i in range(0, len(jogadorAtual.maquina[f"{jogadorAtual.estadoAtual}"][0])):
        if jogadorAtual.maquina[f"{jogadorAtual.estadoAtual}"][0][i] == leitura:
            estadoAtualjogador.append(jogadorAtual.maquina[f"{jogadorAtual.estadoAtual}"][1][i])
    posicao = random.randint(0, (len(estadoAtualjogador) - 1))
    return estadoAtualjogador[posicao]

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
