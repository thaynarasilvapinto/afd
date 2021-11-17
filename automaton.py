class Automaton:
    def __init__(self, states, alphabet, rules, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.rules = rules
        self.initial_state = initial_state
        self.final_states = final_states