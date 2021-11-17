from model.rule import Rule
from model.automaton import Automaton
import json
from usecase.generete_automaton_use_case import generete_pdf
from usecase.process_sequence_use_case import belongs_to_language


def convert_automaton(body):
    rules = []
    for rule in body["regras"]:
        rules.append(Rule(rule["estadoPartida"], rule["simbolo"], rule["estadosDestino"]))
    automaton = Automaton(body["estados"], list(body["alfabeto"]), rules, body["estadoInicial"], body["estadosFinais"])
    return automaton


def read_file(path):
    imput = open(path)
    body = imput.read()
    imput.close()
    return json.loads(body)


def main():
    body = read_file("input/afd1.json")

    automaton = convert_automaton(body)
    generete_pdf(automaton)

    while(True):
        sequence = input()
        print(belongs_to_language(sequence, automaton))


if __name__ == '__main__':
    main()