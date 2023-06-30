class MooreMachine:
    def __init__(self, nomeJogador, vida, maquina):
        self.nomeJogador = nomeJogador
        self.vida = vida
        self.vidaAtual = vida
        self.maquina = maquina
        self.valorAtributoJogador = None
        self.estadoAtual = None
