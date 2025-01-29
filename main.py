from fastapi import FastAPI, Query
import requests

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

@app.get('/api/hello')
def hello_world():
    '''
    Método de exibição de Hello World
    '''
    return {'Hello':'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint de retorno dos restaurantes

    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                prato_restaurante = item['Item']
                preco_prato_restaurante = item['price']
                descricao_prato_restaurante = item['description']
            
                dados_restaurante.append({
                    'item': prato_restaurante,
                    'price': preco_prato_restaurante, 
                    'description': descricao_prato_restaurante
                })
        return {'Restaurante': restaurante,
            'Cardapio':dados_restaurante}
    else:
        return {'Erro': f'{response.status_code}',
                'Mensagem': f'{response.text}'}