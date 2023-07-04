from Responder.response import Response
import os

class ListArquivos:
    def list(self):
        response = Response()
        caminho = "teste/"
        try:
            arquivos = os.listdir(caminho)
        except OSError as e:
            print(f"Erro ao acessar a pasta: {e}")

        if arquivos:
            print("Arquivos disponíveis na pasta:")
            data = []
            for arquivo in arquivos:
                print(arquivo)
                data.append(arquivo)
        else:
            print("Nenhum arquivo encontrado.")

        return response.formatArquivos(data)

