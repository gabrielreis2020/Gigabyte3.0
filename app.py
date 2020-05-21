from flask import Flask, render_template, request, redirect
app = Flask(__name__)


Tabela = [
        ['Refrigerante', 4.50],
        ['Pizza', 2.50],
        ['Suco', 24.90],
        ['Salgado',	5.50],
        ['Lanche', 18.50   ]
]

@app.route('/')
def index():   
    return render_template(
        'index.html',
        titulo='Tabela de Preços',
        Tabela=Tabela
    )

@app.route('/prod/<int:id>')
def produtos(id):
    produ = Tabela[id]
    return render_template(
        'prod.html',
        preco = produ
       
    )

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/store', methods=['POST'])
def store():
    nome = request.form['nome']
    item = request.form['item']

    Tabela.append([nome, item])
    return redirect('/')
    
@app.route('/delete/<int:id>')
def delete(id):
    del Tabela[id]
    return redirect('/')
    
if __name__ == '__main__':
    app.run()