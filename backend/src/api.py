from flask import Flask, request, jsonify
from Action.action import SaveAction

app = Flask(__name__)

@app.route('/saveMooreMachine', methods=['POST'])
def saveMooreMachine():
    save = SaveAction()
    request_data = request.get_json()
    response = save.action(request_data)
    return response, 201

@app.route('/readMachhine', methods=['POST'])
def readMachine():
    return 'Hello, World!'

@app.route('/play', methods=['POST'])
def play():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
