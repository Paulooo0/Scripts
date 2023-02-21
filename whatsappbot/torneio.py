import csv
import random

participantes = {() : 'nome'}

file = open('participantes.csv', 'r')
reader = csv.reader(file)
    
dict = {}
for row in reader:
    key = row[0]
    value = row[1]
    dict[key] = value

unique_list = []
while len(unique_list) < len(dict.keys())*2:
    key_random = random.choice(list(dict.keys()))
    value_random = random.choice(list(dict.values()))
    if (key_random not in unique_list) and (value_random not in unique_list):
        unique_list.append(key_random)
        unique_list.append(value_random)
        print('Chave aleatória: ', key_random) 
        print('Valor aleatório: ', value_random)



