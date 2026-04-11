from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3000}
]

@app.route('/api')
def home():
    return jsonify({"mensagem": "Minha API funcionando"})

@app.route('/produtos', methods=['GET'])
def listar():
    return jsonify(produtos)

@app.route('/produtos', methods=['POST'])
def adicionar():
    novo = request.json
    produtos.append(novo)
    return jsonify({"mensagem": "Adicionado com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
