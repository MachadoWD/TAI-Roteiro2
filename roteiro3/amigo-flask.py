from flask import Flask

app = Flask("site maneiro")


@app.route("/teste")
def teste():
    return "Olá, mundo"

app.run(debug=True)