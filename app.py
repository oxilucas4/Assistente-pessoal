from flask import Flask, request, render_template_string

app = Flask(__name__)

# Função do seu assistente
def seu_assistente(pergunta):
    # Aqui você coloca o que o assistente deve fazer
    if pergunta.lower() == "olá":
        return "Olá! Como posso te ajudar hoje?"
    elif pergunta.lower() == "qual é seu nome?":
        return "Eu sou seu assistente pessoal!"
    else:
        return "Desculpe, não entendi. Pode repetir?"

# Página inicial
@app.route('/', methods=['GET', 'POST'])
def home():
    resposta = ''
    if request.method == 'POST':
        pergunta = request.form['pergunta']
        resposta = seu_assistente(pergunta)
    return render_template_string('''
        <h1>Assistente Pessoal</h1>
        <form method="post">
            <input type="text" name="pergunta" placeholder="Faça sua pergunta">
            <input type="submit" value="Enviar">
        </form>
        <h2>{{ resposta }}</h2>
    ''', resposta=resposta)

if __name__ == '__main__':
    app.run(debug=True)