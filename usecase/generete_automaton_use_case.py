from graphviz import Source, Digraph


def generete_pdf(automato):
    f = Digraph('finite_state_machine', filename='afd')
    f.attr(rankdir='LR', size='8,5')

    f.attr('node', shape='doublecircle')
    for final_states in automato.final_states:
        f.node(final_states)

    f.attr('node', shape='point')
    f.node('qi')

    f.attr('node', shape='circle')
    f.edge('qi', automato.initial_state)
    # todo: melhorar estado inicial
    for rule in automato.rules:  # todo: para transições que aceitem mais de um simbolo, ver como tratar
        f.edge(rule.source_state, rule.targets_state, rule.symbol)

    # todo: entender o porque esta estourando uma exceção
    f.render()