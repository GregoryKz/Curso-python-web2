import requests

BASE_URL = "http://127.0.0.1:5000/api"
LIMITE_ESTOQUE_BAIXO = 5

def obter_todas_pecas():
    try:
        resp = requests.get(f"{BASE_URL}/pecas", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except:
        return []

def classificar_pecas():
    pecas = obter_todas_pecas()
    resultado = {'ok': [], 'baixo': [], 'zerado': []}

    for p in pecas:
        if p['quantidade'] == 0:
            resultado['zerado'].append(p)
        elif p['quantidade'] <= LIMITE_ESTOQUE_BAIXO:
            resultado['baixo'].append(p)
        else:
            resultado['ok'].append(p)

    return resultado

def calcular_valor_total_estoque():
    pecas = obter_todas_pecas()

    total = sum(
        float(p['preco']) * int(p['quantidade'])
        for p in pecas
    )

    return round(total, 2)
def cadastrar_peca(dados):
    try:
        resp = requests.post(f"{BASE_URL}/pecas", json=dados)
        resp.raise_for_status()
        return {'ok': True, 'mensagem': 'Cadastrado!'}
    except Exception as e:
        return {'ok': False, 'mensagem': str(e)}

def buscar_por_categoria(categoria):
    pecas = obter_todas_pecas()
    return [p for p in pecas if p.get('categoria', '').lower() == categoria.lower()]