import re

expressaoRegularPadrao = r'^\w'

class LeituraMaquina:
    def obterEstadoInicial(maquina):
        keysMaquina = maquina.keys()
        keysMaquina = list(keysMaquina)
        estadoInicialMaquina = ""
        for key in keysMaquina:
            primeiraLetra = re.search(expressaoRegularPadrao, key)
            primeiraLetra = primeiraLetra.group()
            if(primeiraLetra == "I"):
                estadoInicialMaquina = key
        return estadoInicialMaquina


    def leituraArquivoMoore(filename):
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
    
    def getPleam(maquina, numeroTransicao, leitura, estadoAtualMaquina, vidaJogador):
        for i in range(0, len(numeroTransicao)):
            if maquina[f"{estadoAtualMaquina}"][0][i] == leitura and vidaJogador != 0:
                estadoAtualAUX1  = maquina[f"{estadoAtualMaquina}"][1][i]
                pleam = re.search(expressaoRegularPadrao, estadoAtualAUX1)
                pleam = pleam.group()

        return pleam