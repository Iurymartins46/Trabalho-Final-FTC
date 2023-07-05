from Service.leituraMaquina import LeituraMaquina
from Service.manipularBanco import MaipulaBanco
from Domain.machine import Machine
from Responder.response import Response
import random, re

expressaoRegularPadrao = r'^\w'
banco = MaipulaBanco()
leitura = LeituraMaquina()

class Batalha:
    def leituraMaquina(self, request):
        player1 = request.json.get('player1')
        player2 = request.json.get('player2')

        maquina1 = leitura.leituraArquivo(player1)
        maquina2 = leitura.leituraArquivo(player2)

        jogador1 = Machine("Arazeal", 50, maquina1)
        jogador2 = Machine("Nehrim", 50, maquina2)

        jogador1.estadoAtual = leitura.obterEstadoInicial(maquina1)
        jogador2.estadoAtual = leitura.obterEstadoInicial(maquina2)

        rodadaDoJogador = random.randint(1, 2)
        outroJogador = 0
        numerosTransicao = maquina1["transicao"]

        banco.saveJson(rodadaDoJogador, True, True, outroJogador, jogador1, jogador2, True, None)

        response = Response()
        return response.formatPlayerInfo(jogador1, jogador2, rodadaDoJogador, True, None)

    def rodada(self, request):
        leituraMaquina = LeituraMaquina()

        rodadaDoJogador, jogadaJogador1Executar, jogadaJogador2Executar, outroJogador, jogador1, jogador2, continuar, vencedor = banco.consumeJson()

        print(continuar)
        if (continuar == True):
            if rodadaDoJogador == 1:
                outroJogador = 2
            else:
                outroJogador = 1

            leitura = request.json.get('entrada')

            jogador1.valorAtributoJogador = random.randint(1, 10)
            proximoEstadoJogador1 = leituraMaquina.obterAtualEstadoJogador(jogador1, leitura)

            jogador2.valorAtributoJogador = random.randint(1, 10)
            proximoEstadoJogador2 = leituraMaquina.obterAtualEstadoJogador(jogador2, leitura)

            if rodadaDoJogador == 1:
                if jogadaJogador1Executar == True:
                    self.executaJogada(jogador1, jogador2, proximoEstadoJogador1, proximoEstadoJogador2)
                if jogadaJogador2Executar == True:
                    self.executaJogada(jogador2, jogador1, proximoEstadoJogador2, proximoEstadoJogador1)
                if jogador1.vidaAtual == 0:
                    jogadaJogador1Executar = False
                if jogador2.vidaAtual == 0:
                    jogadaJogador2Executar = False

            else:
                if jogadaJogador2Executar == True:
                    self.executaJogada(jogador2, jogador1, proximoEstadoJogador2, proximoEstadoJogador1)
                if jogadaJogador1Executar == True:
                    self.executaJogada(jogador1, jogador2, proximoEstadoJogador1, proximoEstadoJogador2)
                if jogador1.vidaAtual == 0:
                    jogadaJogador1Executar = False
                if jogador2.vidaAtual == 0:
                    jogadaJogador2Executar = False

            continuar = None
            if rodadaDoJogador == 1:
                continuar, vencedor = self.condicaoParada(jogador1, jogador2)
            else:
                continuar, vencedor = self.condicaoParada(jogador2, jogador1)

            aux = outroJogador
            outroJogador = rodadaDoJogador
            rodadaDoJogador = aux

            banco.saveJson(rodadaDoJogador, jogadaJogador1Executar, jogadaJogador2Executar, outroJogador, jogador1, jogador2, continuar, vencedor)

        reponse = Response()
        return reponse.formatPlayerInfo(jogador1, jogador2, rodadaDoJogador, continuar, vencedor)


    def executaJogada(self, jogadorAtual, outroJogador, proximoEstadoJogador, proximoEstadoOutroJogador):
        pleaJogadorAtual = self.obterPrimeiraLetraString(proximoEstadoJogador)  # Primeira letra do estado atual do jogador
        pleaOutroJogador = self.obterPrimeiraLetraString(proximoEstadoOutroJogador)  # Primeira letra do estado atual do outro jogador

        mensaguemJogador = None
        if pleaJogadorAtual != "E" and pleaJogadorAtual != "F":
            jogadorAtual.estadoAtual = proximoEstadoJogador
            if pleaJogadorAtual == "A":
                outroJogador.vidaAtual -= jogadorAtual.valorAtributoJogador
                if pleaOutroJogador == "D":
                    if jogadorAtual.valorAtributoJogador >= outroJogador.valorAtributoJogador:
                        outroJogador.vidaAtual += outroJogador.valorAtributoJogador
                    else:
                        outroJogador.vidaAtual += jogadorAtual.valorAtributoJogador
                if outroJogador.vidaAtual <= 0:
                    outroJogador.vidaAtual = 0

            elif pleaJogadorAtual == "C":
                jogadorAtual.vidaAtual += jogadorAtual.valorAtributoJogador
                if (jogadorAtual.vidaAtual > jogadorAtual.vida):
                    jogadorAtual.vidaAtual = jogadorAtual.vida

            elif pleaJogadorAtual == "D":
                mensaguemJogador = ""

        elif pleaJogadorAtual == "E":
            mensaguemJogador = ""

        elif pleaJogadorAtual == "F":
            jogadorAtual.estadoAtual = proximoEstadoJogador

    def condicaoParada(self, jogadorAtual, outroJogador):
        vencedor = None
        maquina1TemEstadoFinal = self.maquinaTemEstadoFinal(jogadorAtual)
        maquina2TemEstadoFinal = self.maquinaTemEstadoFinal(outroJogador)
        pleaJogadorAtual = self.obterPrimeiraLetraString(jogadorAtual.estadoAtual)  # Primeira letra do estado atual do jogador
        pleaOutroJogador = self.obterPrimeiraLetraString(outroJogador.estadoAtual)  # Primeira letra do estado atual do outro jogador

        if maquina1TemEstadoFinal == True and maquina2TemEstadoFinal == True:
            if pleaJogadorAtual == "F":
                vencedor = jogadorAtual.nomeJogador
                return False, vencedor
            elif pleaOutroJogador == "F":
                vencedor = outroJogador.nomeJogador
                return False, vencedor
            elif jogadorAtual.vidaAtual == 0 and outroJogador.vidaAtual == 0:
                vencedor = -1
                return False, vencedor

        elif outroJogador.vidaAtual == 0 or pleaJogadorAtual == "F":
            vencedor = jogadorAtual.nomeJogador
            return False, vencedor
        elif jogadorAtual.vidaAtual == 0 or pleaOutroJogador == "F":
            vencedor = outroJogador.nomeJogador
            return False, vencedor
        return True, vencedor

    def maquinaTemEstadoFinal(self, jogador):
        keysMaquina = jogador.maquina.keys()
        keysMaquina = list(keysMaquina)
        for key in keysMaquina:
            primeiraLetra = self.obterPrimeiraLetraString(key)
            if (primeiraLetra == "F"):
                return True
        return False

    def obterPrimeiraLetraString(self, string):
        primeiraLetra = re.search(expressaoRegularPadrao, string)
        primeiraLetra = primeiraLetra.group()
        return primeiraLetra