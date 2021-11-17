class Automaton:
    def __init__(self, states, alphabet, rules, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.rules = rules
        self.initial_state = initial_state
        self.final_states = final_states


class Rule:
    def __init__(self, source_state, symbol, targets_state):
        self.source_state = source_state
        self.symbol = symbol
        self.targets_state = targets_state
