import csv
import random

irg_list = []

with open('irregular_verbs.csv', 'r') as irg_csv:
    irg_reader = csv.reader(irg_csv, delimiter=';')
    
    for verbs in irg_reader:
        irg_list.append(verbs)

def multiple_answers(object):
    list = object.split("/")
    return list

def random_verb(self):
    x = random.randint(0, 96)
    return self[x]
