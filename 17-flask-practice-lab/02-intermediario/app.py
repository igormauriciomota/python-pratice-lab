
# Importa a classe 'Flask' e a função 'render_template' do modulo 'flask'
# 'Flask' é usado para criar instancias de aplicativos web.
#"Render_template" é usado para renderizar templetes HTML.
from flask import Flask, render_template

# Cria uma instancia da classe Flask.
# '__name__' é uma variavel especial do Python que é
# usada para determinar o nome do modulo atual, isso é necessario para que o flask saiba onde
# encontrar arquivos de template e estaticos.
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)