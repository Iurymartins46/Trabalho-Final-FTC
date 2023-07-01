from Service.leituraMaquina import LeituraMaquina
from Domain.machine import Machine
from Responder.response import Response
import random, json, re
expressaoRegularPadrao = r'^\w'

class Batalha:
    def leituraMaquina(self, request):
        leitura = LeituraMaquina()
        player1 = request.json.get('player1')
        player2 = request.json.get('player2')

        maquina1 = leitura.leituraArquivo(player1)
        maquina2 = leitura.leituraArquivo(player2)

        jogador1 = Machine("Arazeal", 10, maquina1)
        jogador2 = Machine("Nehrim", 10, maquina2)

        jogador1.estadoAtual = leitura.obterEstadoInicial(maquina1)
        jogador2.estadoAtual = leitura.obterEstadoInicial(maquina2)

        rodadaDoJogador = random.randint(1, 2)
        outroJogador = 0
        numerosTransicao = maquina1["transicao"]

        dicionario = dict()
        dicionario['rodadaDoJogador'] = rodadaDoJogador
        dicionario['jogadaJogador1Executar'] = True
        dicionario['jogadaJogador2Executar'] = True
        dicionario['outroJogador'] = outroJogador

        dicionario['nomePlayer1'] = jogador1.nomeJogador
        dicionario['vidaPlayer1'] = jogador1.vida
        dicionario['vidaAtualPlayer1'] = jogador1.vidaAtual
        dicionario['maquinaPlayer1'] = jogador1.maquina
        dicionario['valorAtributoPlayer1'] = jogador1.valorAtributoJogador
        dicionario['estadoAtualPlayer1'] = jogador1.estadoAtual

        dicionario['nomePlayer2'] = jogador2.nomeJogador
        dicionario['vidaPlayer2'] = jogador2.vida
        dicionario['vidaAtualPlayer2'] = jogador2.vidaAtual
        dicionario['maquinaPlayer2'] = jogador2.maquina
        dicionario['valorAtributoPlayer2'] = jogador2.valorAtributoJogador
        dicionario['estadoAtualPlayer2'] = jogador2.estadoAtual

        with open('backend/DataBase/dicionario.json', 'w') as arquivo:
            json.dump(dicionario, arquivo)

        response = Response()
        return response.formatPlayerInfo(jogador1, jogador2, rodadaDoJogador)

    def rodada(self, request):
        leituraMaquina = LeituraMaquina()

        dicionario = dict()
        with open('backend/DataBase/dicionario.json', 'r') as arquivo:
            dicionario = json.load(arquivo)

        rodadaDoJogador = dicionario['rodadaDoJogador']
        jogadaJogador1Executar = dicionario['jogadaJogador1Executar']
        jogadaJogador2Executar = dicionario['jogadaJogador2Executar']
        outroJogador = dicionario['outroJogador']

        jogador1 = Machine(dicionario['nomePlayer1'], dicionario['vidaPlayer1'], dicionario['maquinaPlayer1'])
        jogador1.vidaAtual = dicionario['vidaAtualPlayer1']
        jogador1.valorAtributoJogador = dicionario['valorAtributoPlayer1']
        jogador1.estadoAtual = dicionario['estadoAtualPlayer1']

        jogador2 = Machine(dicionario['nomePlayer2'], dicionario['vidaPlayer2'], dicionario['maquinaPlayer2'])
        jogador2.vidaAtual = dicionario['vidaAtualPlayer2']
        jogador2.valorAtributoJogador = dicionario['valorAtributoPlayer2']
        jogador2.estadoAtual = dicionario['estadoAtualPlayer2']

        if rodadaDoJogador == 1:
            outroJogador = 2
        else:
            outroJogador = 1

        leitura = request.json.get('entrada')

        jogador1.valorAtributoJogador = random.randint(1, 10)
        proximoEstadoJogador1 = leituraMaquina.obterAtualEstadoJogador(jogador1, jogador1.maquina["transicao"], leitura)

        jogador2.valorAtributoJogador = random.randint(1, 10)
        proximoEstadoJogador2 = leituraMaquina.obterAtualEstadoJogador(jogador2, jogador1.maquina["transicao"], leitura)

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
            continuar = self.condicaoParada(jogador1, jogador2)
        else:
            continuar = self.condicaoParada(jogador2, jogador1)

        aux = outroJogador
        outroJogador = rodadaDoJogador
        rodadaDoJogador = aux

        dicionario = dict()
        dicionario['rodadaDoJogador'] = rodadaDoJogador
        dicionario['jogadaJogador1Executar'] = jogadaJogador1Executar
        dicionario['jogadaJogador2Executar'] = jogadaJogador2Executar
        dicionario['outroJogador'] = outroJogador

        dicionario['nomePlayer1'] = jogador1.nomeJogador
        dicionario['vidaPlayer1'] = jogador1.vida
        dicionario['vidaAtualPlayer1'] = jogador1.vidaAtual
        dicionario['maquinaPlayer1'] = jogador1.maquina
        dicionario['valorAtributoPlayer1'] = jogador1.valorAtributoJogador
        dicionario['estadoAtualPlayer1'] = jogador1.estadoAtual

        dicionario['nomePlayer2'] = jogador2.nomeJogador
        dicionario['vidaPlayer2'] = jogador2.vida
        dicionario['vidaAtualPlayer2'] = jogador2.vidaAtual
        dicionario['maquinaPlayer2'] = jogador2.maquina
        dicionario['valorAtributoPlayer2'] = jogador2.valorAtributoJogador
        dicionario['estadoAtualPlayer2'] = jogador2.estadoAtual

        with open('backend/DataBase/dicionario.json', 'w') as arquivo:
            json.dump(dicionario, arquivo)

        reponse = Response()
        return reponse.formatPlayerInfo(jogador1, jogador2, rodadaDoJogador)


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
                return False
            elif pleaOutroJogador == "F":
                vencedor = outroJogador.nomeJogador
                return False
            elif jogadorAtual.vidaAtual == 0 and outroJogador.vidaAtual == 0:
                vencedor = -1
                return False

        elif outroJogador.vidaAtual == 0 or pleaJogadorAtual == "F":
            vencedor = jogadorAtual.nomeJogador
            return False
        elif jogadorAtual.vidaAtual == 0 or pleaOutroJogador == "F":
            vencedor = outroJogador.nomeJogador
            return False
        return True

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