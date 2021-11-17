from rule import Rule

covered_rules = []


def belongs_to_language(sequence, automaton):
    end_state = process_sequence(list(sequence), automaton.initial_state, automaton.rules)
    return is_acceptable_states(end_state, automaton.final_states)


def process_sequence(sequence, inicial_state, rules):
    current_state = inicial_state
    for current_symbol in sequence:
        rule = applicable_rule(rules, current_state, current_symbol)
        add_covered_rule(rule)
        current_state = apply_rule(rule)
    return current_state


def applicable_rule(rules, current_state, current_symbol):
    for rule in rules:
        if is_rule_applicable(rule, current_state, current_symbol):
            return rule
    return None


def is_rule_applicable(rule, current_state, current_symbol):
    return rule.source_state == current_state and rule.symbol == current_symbol


def apply_rule(rule):
    return rule.targets_state


def is_acceptable_states(state, acceptable_states):
    return state in acceptable_states


def add_covered_rule(rule):
    covered_rules.append(rule)


def get_covered_rule():
    return covered_rules
