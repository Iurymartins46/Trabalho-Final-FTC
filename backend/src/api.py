from flask import Flask, request, jsonify
from flask_cors import CORS
from Action.action import SaveAction
from Action.listArquivos import ListArquivos

app = Flask(__name__)
CORS(app)

@app.route('/listarArquivos', methods=['GET'])
def listarArquivos():
    arq = ListArquivos()
    return arq.list()

if __name__ == '__main__':
    app.run()
