from flask import Flask, request, jsonify
from flask_cors import CORS
from Action.listArquivos import ListArquivos
from Action.batalha import Batalha

app = Flask(__name__)
CORS(app)

@app.route('/listarArquivos', methods=['GET'])
def listarArquivos():
    arq = ListArquivos()
    return arq.list(), 200

@app.route('/escolherMaquina', methods=['POST'])
def escolherMaquina():
    btl = Batalha()
    return btl.leituraMaquina(request), 200

@app.route('/rodada', methods=['POST'])
def rodada():
    btl = Batalha()
    return btl.rodada(request), 200

if __name__ == '__main__':
    app.run()
