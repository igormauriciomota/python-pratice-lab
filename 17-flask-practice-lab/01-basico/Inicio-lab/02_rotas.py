from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Pagina inicial"

@app.route("/sobre")
def sobre():
    return "Página Sobre"

@app.route("/contato")
def contato():
    return "Página contato"

if __name__ == "__main__":
    app.run(debug=True)

