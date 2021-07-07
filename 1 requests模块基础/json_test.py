import json

filename = 'dog.json'

file = open(filename, 'r', encoding='utf-8')
dict = json.load(file)
print(dict.keys())
file.close()