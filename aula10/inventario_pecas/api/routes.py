from flask import Blueprint, jsonify, request
from database.conexao import get_connection

api_blueprint = Blueprint('api', __name__)

# LISTAR PEÇAS
@api_blueprint.route('/pecas', methods=['GET'])
def listar_pecas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pecas ORDER BY nome")
    dados = cursor.fetchall()
    conn.close()
    return jsonify(dados)

# BUSCAR POR CÓDIGO
@api_blueprint.route('/pecas/<codigo>', methods=['GET'])
def buscar_peca(codigo):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pecas WHERE codigo=%s", (codigo,))
    peca = cursor.fetchone()
    conn.close()

    if not peca:
        return jsonify({'erro': 'Peça não encontrada'}), 404

    return jsonify(peca)

# CADASTRAR
@api_blueprint.route('/pecas', methods=['POST'])
def cadastrar_peca():
    dados = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO pecas (codigo, nome, veiculo, categoria, preco, quantidade)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (
        dados['codigo'],
        dados['nome'],
        dados.get('veiculo', 'Gol Quadrado'),
        dados.get('categoria', 'Geral'),
        dados['preco'],
        dados['quantidade']
    ))

    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'Peça cadastrada!'}), 201

# DELETE
@api_blueprint.route('/pecas/<codigo>', methods=['DELETE'])
def deletar_peca(codigo):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM pecas WHERE codigo=%s", (codigo,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({'erro': 'Peça não encontrada'}), 404

    cursor.execute("DELETE FROM pecas WHERE codigo=%s", (codigo,))
    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'Peça removida!'}) 