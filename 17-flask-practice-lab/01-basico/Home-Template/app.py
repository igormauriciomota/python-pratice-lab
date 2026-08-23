from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # A rota envia dados Python para HTML usando jinja2.
    tecnologias = ['Python', 'Flask', 'HTML', 'CSS', 'jinja2']
    return render_template('index.html', tecnologias=tecnologias)

if __name__ == '__main__':
    app.run(debug=True)
    