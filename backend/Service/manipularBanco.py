import json
from Domain.machine import Machine

class MaipulaBanco:
    def consumeJson(self):
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

        continuar = dicionario['continuar']
        vencedor = dicionario['vencedor']

        return rodadaDoJogador, jogadaJogador1Executar, jogadaJogador2Executar, outroJogador, jogador1, jogador2, continuar, vencedor

    def saveJson(self, rodadaDoJogador, jogadaJogador1Executar, jogadaJogador2Executar, outroJogador, jogador1, jogador2, continuar, vencedor):
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

        dicionario['continuar'] = continuar
        dicionario['vencedor'] = continuar

        with open('backend/DataBase/dicionario.json', 'w') as arquivo:
            json.dump(dicionario, arquivo)