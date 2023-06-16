from Domain.Moore import MooreMachine
from Responder.response import Response

class SaveAction:
    def action(self, request_data):
        more = MooreMachine(request_data['states'], request_data['inputs'], request_data['outputs'], request_data['transitions'], request_data['initial_state'])
        response = Response()
        response = response.formatData(more)
        return response 