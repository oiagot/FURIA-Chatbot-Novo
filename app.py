from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Respostas diretas baseadas em palavras-chave
respostas = {
    "introdução": "Fala, guerreiro! Eu sou a FURIA, o bot oficial da torcida mais insana do CS. Vamos conversar sobre o time mais brabo do cenário!",
    "falar sobre jogos": "A FURIA joga sempre com garra! Nosso próximo desafio é contra a G2, vai ser imperdível!",
    "proximo jogo": "O próximo jogo da FURIA é dia 05/05 às 18h contra a G2.",
    "falar sobre o time": "O time da FURIA é formado por lendas do CS, com o capitão FalleN liderando com maestria!",
    "capitao": "O capitão do time de CS da FURIA é o FalleN.",
    "titulos": "A FURIA já conquistou mais de 10 títulos em torneios nacionais e internacionais.",
    "curiosidade": "Você sabia que a FURIA foi o primeiro time brasileiro a chegar ao top 3 do ranking mundial em 2020?",
}

# Respostas genéricas quando a IA não entende
respostas_genericas = [
    "Essa não deu pra entender, irmão. Manda uma pergunta no estilo campeão! 💪",
    "Não vacila! Pergunta sobre o próximo jogo, o capitão ou os títulos da FURIA. 😤",
    "Tá difícil assim... Fala comigo direito aí, tipo: 'Qual o próximo jogo?' 🎯",
    "Ainda tô aprendendo, mas com treino eu fico sinistro. Tenta de novo! 🔥",
    "Essa passou batida, mas não se preocupa... na próxima eu acerto! 🧠"
]

# Respostas de torcida
respostas_torcida = [
    "FURIAaaa, é nós! Vamos amassar esses caras! 💥",
    "O time tá voando, irmão! Que venha mais um título! 🏆",
    "Vai, FURIA! A torcida tá contigo, sempre! 🔥",
    "A FURIA é a mais forte, vamos esmagar qualquer time! 💪",
    "Quem duvida da FURIA? Tá vendo o jogo? Tá chegando a hora! ⚡"
]

# Dados sobre os jogos
jogos = [
    {
        "id": 1,
        "time1": "FURIA",
        "time2": "G2",
        "data": "2025-05-05 18:00",
        "status": "Em andamento",
    },
    {
        "id": 2,
        "time1": "FURIA",
        "time2": "Astralis",
        "data": "2025-05-10 16:00",
        "status": "Próximo jogo",
    }
]

@app.route("/responder", methods=["POST"])
def responder():
    mensagem = request.json["mensagem"].lower()

    for chave in respostas:
        if chave in mensagem:
            return jsonify({"resposta": respostas[chave]})

    resposta = random.choice(respostas_torcida + respostas_genericas)
    return jsonify({"resposta": resposta})

@app.route("/jogo/atual", methods=["GET"])
def jogo_atual():
    return jsonify(jogos[0])

@app.route("/jogo/proximo", methods=["GET"])
def proximo_jogo():
    return jsonify(jogos[1])

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
