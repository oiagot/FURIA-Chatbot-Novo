from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Respostas simples
respostas = {
    "proximo jogo": "O próximo jogo da FURIA é dia 05/05 às 18h contra a G2.",
    "capitao": "O capitão do time de CS da FURIA é o FalleN.",
    "titulos": "A FURIA já conquistou mais de 10 títulos em torneios nacionais e internacionais.",
    "curiosidade": "Você sabia que a FURIA foi o primeiro time brasileiro a chegar ao top 3 do ranking mundial em 2020?",
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/responder", methods=["POST"])
def responder():
    mensagem = request.json["mensagem"].lower()
    for chave in respostas:
        if chave in mensagem:
            return jsonify({"resposta": respostas[chave]})
    return jsonify({"resposta": "Desculpa, não entendi. Tente perguntar sobre o 'próximo jogo', 'capitão', 'títulos' ou 'curiosidades'."})

if __name__ == "__main__":
    app.run(debug=True)