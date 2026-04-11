from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tarefa = request.form.get('tarefa')

        if tarefa.strip():
            tarefas.append(tarefa.strip())

        return redirect('/')

    return render_template('index.html', tarefas=tarefas)

if __name__ == '__main__':
    app.run(debug=True)