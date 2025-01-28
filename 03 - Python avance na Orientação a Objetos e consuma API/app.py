import requests


url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    print('Ok')
    dados_json = response.json()
    dados_restaurante = {}

    for item in dados_json:
        nome_restaurante = item['Company']
        prato_restaurante = item['Item']
        preco_prato_restaurante = item['price']
        descricao_prato_restaurante = item['description']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
        dados_restaurante[nome_restaurante].append({
            'item': prato_restaurante,
            'price': preco_prato_restaurante, 
            'description': descricao_prato_restaurante
        })
else:
    print(f'Erro: {response.status_code}')

print(dados_restaurante['Pizza Hut'])