"""
Aplicação Flask - Sistema de Navegação com Templates

Este arquivo é responsável por inicializar a aplicação Flask
e definir as rotas principais do sistema.

Funcionalidades:
- Criação da aplicação Flask.
- Definição das rotas da aplicação.
- Renderização de páginas HTML utilizando templates.
- Navegação entre diferentes páginas do sistema.
- Inicialização do servidor de desenvolvimento.

Rotas disponíveis:
    /       -> Página inicial (index.html)
    /page1  -> Página 1 (page1.html)
    /page2  -> Página 2 (page2.html)

Tecnologias utilizadas:
- Python
- Flask
- HTML
- Jinja2

Objetivo:
Praticar os fundamentos do Flask, principalmente rotas,
funções de visualização e renderização de templates HTML.

"""
# Importa a classe 'Flask' e a função 'render_template' do modulo 'flask'
# 'Flask' é usado para criar instancias de aplicativos web.
#"Render_template" é usado para renderizar templetes HTML.

from flask import Flask, render_template

# Cria uma instancia da classe Flask.
# '__name__' é uma variavel especial do Python que é
# usada para determinar o nome do modulo atual, isso é necessario para que o flask saiba onde
# encontrar arquivos de template e estaticos.

app = Flask(__name__)

@app.route('/')

def home():

    return render_template('home.html')

@app.route('/page1')


# Define a função "page1", que será chamada quando a URL "/page1" for acessada.
def page1():

    # Renderiza o arquivo de template 'page1.html' e o
    # retorna ao navegador.
    return render_template('page1.html')

# Decorador que associa a função "page2 a URL "/page2".

@app.route('/page2')

# Define a função "page2", que será chamada quando a URL "/page2" for acessada.
def page2():

    return render_template('page2.html')


# verifica se o script está sendo executado com o script
# principal e não sendo importado como um modulo.
if __name__ == '__main__':

    # Inicia o servidor web do Flask.
    # 'debug=True' ativa o modulo de depuração o que e
    # util durante o desenvolvimento
    app.run(debug=True)

