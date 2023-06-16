from flask import Flask, request, jsonify
from Action.action import SaveAction

app = Flask(__name__)

@app.route('/saveMooreMachine', methods=['POST'])
def saveMooreMachine():
    save = SaveAction()
    request_data = request.get_json()
    response = save.action(request_data)
    return response, 201

if __name__ == '__main__':
    app.run()
