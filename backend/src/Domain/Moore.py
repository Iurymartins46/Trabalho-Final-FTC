class MooreMachine:
    def __init__(self, states, inputs, outputs, transitions, initial_state):
        self.states = states
        self.inputs = inputs
        self.outputs = outputs
        self.transitions = transitions
        self.current_state = initial_state

    def process_input(self, input_value):
        if input_value not in self.inputs:
            raise ValueError("Invalid input")

        if self.current_state not in self.transitions:
            raise ValueError("Invalid current state")

        next_state = self.transitions[self.current_state][input_value]
        output = self.outputs[next_state]

        self.current_state = next_state

        return output