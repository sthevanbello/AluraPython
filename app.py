import requests
import json


url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
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

for nome_restaurante, dados in dados_restaurante.items():
    print(nome_restaurante)
    nome_arquivo = f'{nome_restaurante}.json'
    with open(nome_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)