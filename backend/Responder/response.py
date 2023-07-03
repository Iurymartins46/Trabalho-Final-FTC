import json
from Domain.machine import Machine

class Response:
    def formatArquivos(self, arquivos):
        data = {
            "status" : "Deu bom",
            "arquivos" : arquivos
        }

        return data

    def formatPlayerInfo(self, player1, player2, rodadaDoJogador, continuar, vencedor):
        data = {
            "player1" : {
                "nomeJogador": player1.nomeJogador,
                "vida": player1.vida,
                "vidaAtual": player1.vidaAtual,
                "valorAtributoJogador": player1.valorAtributoJogador,
                "estadoAtual": player1.estadoAtual
            },
            "player2" : {
                "nomeJogador": player2.nomeJogador,
                "vida": player2.vida,
                "vidaAtual": player2.vidaAtual,
                "valorAtributoJogador": player2.valorAtributoJogador,
                "estadoAtual": player2.estadoAtual
            },
            "rodadaDoJogador" : rodadaDoJogador,
            "continuar": continuar,
            "vencedor": vencedor
        }

        return data
