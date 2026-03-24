from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, World!</h1><p>meu primeiro site</p>"

@app.route("/contato")
def contato():
    return "Qualquer dúvida mande um e-mail para suporte@faculdade.com.br"


if __name__ == "__main__":
    app.run(debug=True)