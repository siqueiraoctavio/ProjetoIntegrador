from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def header():
    return render_template("header.html")

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar.html")

@app.route("/consultar")
def consultar():
    return render_template("consultar.html")

@app.route("/edicao")
def Edicao():
    return render_template("Edicao.html")


if __name__ == "__main__":
    app.run(debug=True)


