from flask import Flask, request, render_template_string

app = Flask(__name__)

# Função do assistente com a nova personalidade
def seu_assistente(pergunta):
    # Respostas baseadas no que for perguntado
    if pergunta.lower() == "olá":
        return "Olá divos e divas! Como posso ajudá-los hoje?"
    elif pergunta.lower() == "qual é seu nome?":
        return "Eu sou o Divo, seu assistente pessoal!"
    else:
        return "Desculpe, não entendi. Pode repetir, divo/diva?"

# Página inicial
@app.route('/', methods=['GET', 'POST'])
def home():
    resposta = ''
    if request.method == 'POST':
        pergunta = request.form['pergunta']
        resposta = seu_assistente(pergunta)
    return render_template_string('''
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>EU SOU O DIVO</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f8ff;
                    text-align: center;
                    padding: 20px;
                }
                h1 {
                    color: #ff1493;
                    font-size: 2.5em;
                }
                h2 {
                    color: #8a2be2;
                }
                form {
                    margin-top: 20px;
                }
                input[type="text"] {
                    padding: 10px;
                    width: 300px;
                    font-size: 1.1em;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                }
                input[type="submit"] {
                    padding: 10px 20px;
                    font-size: 1.1em;
                    background-color: #ff1493;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #d11f80;
                }
            </style>
        </head>
        <body>
            <h1>EU SOU O DIVO</h1>
            <p>O assistente pessoal mais divo da internet! 🌟</p>
            <form method="post">
                <input type="text" name="pergunta" placeholder="Faça sua pergunta, divo/diva!">
                <input type="submit" value="Enviar">
            </form>
            <h2>{{ resposta }}</h2>
        </body>
        </html>
    ''', resposta=resposta)

if __name__ == '__main__':
    app.run(debug=True)
