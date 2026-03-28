from flask import Blueprint, render_template, request, redirect, url_for
from backend.servicos import *

frontend_blueprint = Blueprint(
    'frontend',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@frontend_blueprint.route('/')
def index():
    pecas = obter_todas_pecas()
    status = classificar_pecas()
    total = calcular_valor_total_estoque()

    return render_template(
        'index.html',
        pecas=pecas,
        status=status,
        valor_total=total
    )

@frontend_blueprint.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        dados = request.form.to_dict()
        dados['preco'] = float(dados['preco'])
        dados['quantidade'] = int(dados['quantidade'])

        resultado = cadastrar_peca(dados)

        if resultado['ok']:
            return redirect(url_for('frontend.index'))
        else:
            return render_template('cadastrar.html', mensagem=resultado['mensagem'])

    return render_template('cadastrar.html')