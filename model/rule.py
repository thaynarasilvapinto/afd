class Rule:
    def __init__(self, source_state, symbol, targets_state):
        self.source_state = source_state
        self.symbol = symbol
        self.targets_state = targets_state
