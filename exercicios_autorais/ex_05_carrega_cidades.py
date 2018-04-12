import codecs
import json

file_cidades = codecs.open('cidades.json', encoding='utf-8')

cidades_texto = file_cidades.read()
cidades_json = json.loads(cidades_texto)

for cidade in cidades_json:
    print(cidade)
