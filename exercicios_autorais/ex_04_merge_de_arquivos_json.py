import simplejson

lista_de_urls = [
    {'application_id': 1, 'json': '{"/api/v1/produtos": {"metodos": ["GET", "POST"]}}'},
    {'application_id': 1, 'json': '{"/api/v1/produtos": {"metodos": ["PUT", "DELETE"]}}'}
]
nova_lista_de_urls = {}

for url in lista_de_urls:
    application_id = url['application_id']
    rotas = url['json']
    
    for rota, metodos in rotas.items():
        rota = rota.replace('\\d+', 'd+')
        if application_id not in nova_lista_de_urls:
            nova_lista_de_urls[application_id] = {rota: metodos}
        elif rota not in nova_lista_de_urls[application_id]:
            nova_lista_de_urls[application_id][rota] = metodos
        else:
            for metodo in metodos['metodos']:
                if metodo not in nova_lista_de_urls[application_id][rota]['metodos']:
                    nova_lista_de_urls[application_id][rota]['metodos'].append(metodo)

for application_id, rotas in nova_lista_de_urls.items():
    print(application_id, simplejson.dumps(rotas).replace('d+', '\\\\d+'))
