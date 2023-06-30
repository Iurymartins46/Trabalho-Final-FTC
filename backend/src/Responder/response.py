import json

class Response:
    def formatData(self, mooreMachine):
        data = {
            "status": "Salvo com sucesso",
            "type": "MooreMachine",
            "states": mooreMachine.states,
            "inputs": mooreMachine.inputs,
            "outputs": mooreMachine.outputs,
            "transitions": mooreMachine.transitions,
            "initial_state": mooreMachine.current_state
        }
        return data

    def formatArquivos(self, arquivos):
        data = {
            "status" : "Deu bom",
            "arquivos" : arquivos
        }

        return data