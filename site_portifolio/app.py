import os
from flask import Flask, render_template, request, flash, redirect, url_for

# Inicialização da aplicação Flask
app = Flask(__name__)
app.secret_key = 'minha_chave_secreta'

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Página de contato
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        mensagem = request.form['mensagem']

        # Simplesmente exibindo uma mensagem de sucesso (sem envio de email)
        flash(f'Mensagem enviada com sucesso por {nome}!', 'success')
        return redirect(url_for('index'))
    return render_template('contato.html')

# Rodando a aplicação
if __name__ == '__main__':
    app.run(debug=True)
