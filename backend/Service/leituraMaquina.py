import re
import random

expressaoRegularPadrao = r'^\w'

class LeituraMaquina:
    def leituraArquivo(self, filename):
        filename = "teste/" + filename
        print(filename)
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

    def obterPrimeiraLetraString(self, string):
        primeiraLetra = re.search(expressaoRegularPadrao, string)
        primeiraLetra = primeiraLetra.group()
        return primeiraLetra

    def obterEstadoInicial(self, maquina):
        keysMaquina = maquina.keys()
        keysMaquina = list(keysMaquina)
        estadoInicialMaquina = None
        for key in keysMaquina:
            primeiraLetra = self.obterPrimeiraLetraString(key)
            if(primeiraLetra == "I"):
                estadoInicialMaquina = key
                break
        return estadoInicialMaquina

    def obterAtualEstadoJogador(self, jogadorAtual, numerosTransicao, leitura):
        estadoAtualjogador = None
        for i in range(0, len(numerosTransicao)):
            if jogadorAtual.maquina[f"{jogadorAtual.estadoAtual}"][0][i] == leitura:
                estadoAtualjogador = jogadorAtual.maquina[f"{jogadorAtual.estadoAtual}"][1][i]
        return estadoAtualjogador