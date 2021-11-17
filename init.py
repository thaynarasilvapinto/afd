from rule import Rule
from automaton import Automaton
import json
from generete_automaton import generete_pdf
from automaton_service import belongs_to_language


def convert_automaton(body):
    rules = []
    for rule in body["regras"]:
        rules.append(Rule(rule["estadoPartida"], rule["simbolo"], rule["estadosDestino"]))
    automaton = Automaton(body["estados"], list(body["alfabeto"]), rules, body["estadoInicial"], body["estadosFinais"])
    return automaton


def main():
    imput = open("imput.json")
    body = imput.read()
    imput.close()
    body = json.loads(body)

    automaton = convert_automaton(body)
    generete_pdf(automaton)

    while(True):
        sequence = input()
        print(belongs_to_language(sequence, automaton))


if __name__ == '__main__':
    main()