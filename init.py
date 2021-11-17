from model.models import Automaton, Rule
import json
from usecase.generete_automaton_use_case import generete_pdf
from usecase.process_sequence_use_case import belongs_to_language


if __name__ == '__main__':
    main()


def main():
    body = read_file("input/afd2.json")

    automaton = dto_automaton(body)
    generete_pdf(automaton)

    while True:
        sequence = input()
        print(belongs_to_language(sequence, automaton))


def read_file(path):
    with open(path, 'r') as file:
        body = file.read()
    file.close()
    return json.loads(body)


def dto_automaton(body):
    rules = []
    for rule in body["regras"]:
        rules.append(Rule(rule["estadoPartida"], rule["simbolo"], rule["estadosDestino"]))
    automaton = Automaton(body["estados"], list(body["alfabeto"]), rules, body["estadoInicial"], body["estadosFinais"])
    return automaton